from odoo import models, fields


class DwCategory(models.Model):
    _name = 'lamgido.dw.category'
    _description = 'DW Category'
    _order = 'name'

    name = fields.Char(required=True)
    description = fields.Text()
    active = fields.Boolean(default=True)