from odoo import api, exceptions, fields, models, _


class LamgidoDwCategory(models.Model):
    _name = "lamgido.dw.category"
    _description = "DW Category"

    name = fields.Char(required=True)
    code = fields.Char()
    description = fields.Text()
    active = fields.Boolean(default=True)


class LamgidoDwRecord(models.Model):
    _name = "lamgido.dw.record"
    _description = "DW Fact Record"

    name = fields.Char(string="Label")
    date = fields.Date(
        required=True,
        default=fields.Date.context_today,
        copy=False,
    )
    category_id = fields.Many2one(
        "lamgido.dw.category",
        string="Category",
        required=True,
    )
    measure_amount = fields.Float(
        string="Amount",
        help="Main numeric measure",
        readonly=True,
        copy=False,
    )
    measure_qty = fields.Float(
        string="Quantity",
        default=1.0,
    )
    notes = fields.Text()
    active = fields.Boolean(default=True)
    state = fields.Selection(
        [
            ("new", "New"),
            ("validated", "Validated"),
            ("archived", "Archived"),
        ],
        string="Status",
        default="new",
        required=True,
        copy=False,
    )

    def action_validate(self):
        for record in self:
            record.state = "validated"

    def action_archive(self):
        for record in self:
            record.state = "archived"

    @api.constrains("measure_amount", "measure_qty")
    def _check_positive_measures(self):
        for record in self:
            if record.measure_amount < 0 or record.measure_qty < 0:
                raise exceptions.ValidationError(
                    _("Amount and Quantity must be positive.")
                )
