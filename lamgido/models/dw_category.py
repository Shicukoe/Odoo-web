from odoo import models, fields, api
from odoo.exceptions import ValidationError


class DwCategory(models.Model):
    _name = 'lamgido.dw.category'
    _description = 'DW Category'
    _order = 'name'

    name = fields.Char(required=True, default="New")
    description = fields.Text()
    active = fields.Boolean(default=True)

    record_ids = fields.One2many(
        'lamgido.dw.record',
        'category_id',
        string="Records"
    )

    record_count = fields.Integer(
        compute="_compute_record_count"
    )

    def _compute_record_count(self):
        for rec in self:
            rec.record_count = len(rec.record_ids)

    @api.constrains('name')
    def _check_unique_name(self):
        for rec in self:
            domain = [('name', '=', rec.name), ('id', '!=', rec.id)]
            if self.search_count(domain):
                raise ValidationError("Category name must be unique.")