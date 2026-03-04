from odoo import models, fields, api


class DwRecord(models.Model):
    _name = 'lamgido.dw.record'
    _description = 'DW Storage Record'
    _order = 'date desc'

    name = fields.Char(required=True, copy=False, default="New")
    date = fields.Date(required=True, default=fields.Date.context_today)

    category_id = fields.Many2one(
        'lamgido.dw.category',
        required=True,
        ondelete='restrict'
    )

    # 🔹 Quantity should be Integer
    quantity = fields.Integer(required=True, default=1)

    # 🔹 Size per unit
    size_per_unit = fields.Float(required=True)

    # 🔹 Unit selection
    size_unit = fields.Selection([
        ('kb', 'KB'),
        ('mb', 'MB'),
        ('gb', 'GB'),
    ], string="Unit", default='mb', required=True)


    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done')
    ], default='draft')
