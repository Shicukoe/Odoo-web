from odoo import api, exceptions, fields, models, _


class LamgidoDwCategory(models.Model):
    _name = "lamgido.dw.category"
    _description = "DW Category"

    name = fields.Char(required=True)
    description = fields.Text()
    active = fields.Boolean(default=True)


class LamgidoDwRecord(models.Model):
    _name = "lamgido.dw.record"
    _description = "DW Fact Record"
    _order = "date desc"

    name = fields.Char(string="Reference", required=True)

    date = fields.Date(
        required=True,
        default=fields.Date.context_today,
    )

    category_id = fields.Many2one(
        "lamgido.dw.category",
        string="Category",
        required=True,
    )

    quantity = fields.Float(
        string="Quantity",
        required=True,
        default=1.0,
    )

    value_per_unit = fields.Float(
        string="Value per Unit",
        required=True,
    )

    # Chapter 9 computed field
    total_value = fields.Float(
        string="Total Value",
        compute="_compute_total_value",
        store=True,
    )

    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("confirmed", "Confirmed"),
            ("done", "Done"),
        ],
        default="draft",
        required=True,
    )

    # =============================
    # COMPUTE
    # =============================
    @api.depends("quantity", "value_per_unit")
    def _compute_total_value(self):
        for record in self:
            record.total_value = record.quantity * record.value_per_unit

    # =============================
    # ONCHANGE
    # =============================
    @api.onchange("category_id")
    def _onchange_category(self):
        if self.category_id:
            self.name = f"{self.category_id.name}-{fields.Date.today()}"

    # =============================
    # CONSTRAINT
    # =============================
    @api.constrains("quantity", "value_per_unit")
    def _check_positive(self):
        for record in self:
            if record.quantity <= 0 or record.value_per_unit < 0:
                raise exceptions.ValidationError(
                    _("Quantity must be > 0 and Value must be positive.")
                )

    # =============================
    # ACTION BUTTONS (Chapter 8)
    # =============================
    def action_confirm(self):
        self.state = "confirmed"

    def action_done(self):
        self.state = "done"