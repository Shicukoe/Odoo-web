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
    )

    category_id = fields.Many2one(
        "lamgido.dw.category",
        string="Category",
        required=True,
    )

    measure_qty = fields.Float(
        string="Quantity",
        default=1.0,
    )

    unit_price = fields.Float(
        string="Unit Price",
        default=0.0,
    )

    # ✅ Computed field
    measure_amount = fields.Float(
        string="Total Amount",
        compute="_compute_total_amount",
        store=True,   # important for pivot/graph reports
    )

    notes = fields.Text()
    active = fields.Boolean(default=True)

    state = fields.Selection(
        [
            ("new", "New"),
            ("validated", "Validated"),
            ("archived", "Archived"),
        ],
        default="new",
        required=True,
    )

    # ==============================
    # COMPUTE METHOD
    # ==============================
    @api.depends("measure_qty", "unit_price")
    def _compute_total_amount(self):
        for record in self:
            record.measure_amount = record.measure_qty * record.unit_price

    # ==============================
    # ONCHANGE METHOD
    # ==============================
    @api.onchange("category_id")
    def _onchange_category(self):
        if self.category_id:
            self.notes = f"Category selected: {self.category_id.name}"

    # ==============================
    # CONSTRAINT
    # ==============================
    @api.constrains("measure_qty", "unit_price")
    def _check_positive_values(self):
        for record in self:
            if record.measure_qty < 0 or record.unit_price < 0:
                raise exceptions.ValidationError(
                    _("Quantity and Unit Price must be positive.")
                )

    # ==============================
    # ACTION BUTTONS
    # ==============================
    def action_validate(self):
        self.state = "validated"

    def action_archive(self):
        self.state = "archived"