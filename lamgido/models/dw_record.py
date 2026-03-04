from odoo import models, fields


class DwRecord(models.Model):
    _name = 'lamgido.dw.record'
    _description = 'DW Record'
    _order = 'date desc'

    name = fields.Char(required=True, copy=False, default="New")
    date = fields.Date(required=True, default=fields.Date.context_today)

    category_id = fields.Many2one(
        'lamgido.dw.category',
        required=True,
        ondelete='restrict'
    )

    quantity = fields.Float(required=True)
    value_per_unit = fields.Float(required=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done')
    ], default='draft')