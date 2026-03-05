from odoo import Command, models, fields
from odoo.exceptions import UserError


class DwRecordInvoice(models.Model):
    _inherit = 'lamgido.dw.record'

    invoice_id = fields.Many2one(
        'account.move',
        string='Invoice',
        readonly=True,
        copy=False,
        help='Customer invoice created when this record is marked Done.',
    )

    def action_done(self):
        """Create a customer invoice with lines when marked Done."""
        for rec in self:
            if rec.state != 'confirmed':
                continue
            rec._create_invoice_if_needed()
        return super().action_done()

    def _get_invoice_line_account(self):
        """Income account for invoice lines (no product)."""
        account = self.env['account.account'].search(
            [
                ('company_id', '=', self.env.company.id),
                ('account_type', '=', 'income'),
            ],
            limit=1,
        )
        if not account:
            raise UserError(
                'No income account found. Please configure Accounting.'
            )
        return account

    def _create_invoice_if_needed(self):
        """Create out_invoice with two lines: 6% of storage value + 100.00 admin fee."""
        self.ensure_one()
        if self.invoice_id:
            return
        if not self.owner_partner_id:
            raise UserError(
                'Please set an Owner (Customer) on this record before marking it Done.'
            )
        journal = self.env['account.journal'].search(
            [('type', '=', 'sale'), ('company_id', '=', self.env.company.id)],
            limit=1,
        )
        if not journal:
            raise UserError(
                'No sales journal found. Please configure Accounting.'
            )
        income_account = self._get_invoice_line_account()

        # Base "value" for storage (e.g. 0.01 per KB) – 6% of this
        storage_value = self.total_size_kb * 0.01
        storage_fee = round(storage_value * 0.06, 2)
        admin_fee = 100.0

        # Match Odoo 16 account.move flow: pass invoice_date so move date is set;
        # invoice_line_ids only (no line_ids) so _move_autocomplete_invoice_lines_create
        # adds payment terms and balances the move.
        move_vals = {
            'move_type': 'out_invoice',
            'partner_id': self.owner_partner_id.id,
            'journal_id': journal.id,
            'invoice_origin': self.name,
            'invoice_date': fields.Date.context_today(self),
            'invoice_line_ids': [
                Command.create({
                    'name': 'Storage fee (6% of storage value)',
                    'quantity': 1.0,
                    'price_unit': storage_fee,
                    'account_id': income_account.id,
                }),
                Command.create({
                    'name': 'Administrative fees',
                    'quantity': 1.0,
                    'price_unit': admin_fee,
                    'account_id': income_account.id,
                }),
            ],
        }
        move = self.env['account.move'].create(move_vals)
        self.invoice_id = move.id

    def action_open_invoice(self):
        """Open the linked customer invoice (for the stat button)."""
        self.ensure_one()
        if not self.invoice_id:
            return
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'account.move',
            'res_id': self.invoice_id.id,
            'view_mode': 'form',
            'view_type': 'form',
        }

