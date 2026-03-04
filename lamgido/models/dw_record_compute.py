from odoo import models, fields, api


class DwRecordCompute(models.Model):
    _inherit = 'lamgido.dw.record'

    total_size_kb = fields.Float(
        compute='_compute_total_size_kb',
        store=True
    )


    @api.depends('quantity', 'size_per_unit', 'size_unit')
    def _compute_total_size_kb(self):
        for rec in self:
            total = rec.quantity * rec.size_per_unit

            if rec.size_unit == 'gb':
                total = total * 1024 * 1024
            elif rec.size_unit == 'mb':
                total = total * 1024
            # kb stays as is

            rec.total_size_kb = total