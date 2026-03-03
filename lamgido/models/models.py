# -*- coding: utf-8 -*-
from odoo import models, fields


class LamgidoDwCategory(models.Model):
    _name = 'lamgido.dw.category'
    _description = 'DW Category'

    name = fields.Char(required=True)
    code = fields.Char()
    description = fields.Text()
    active = fields.Boolean(default=True)


class LamgidoDwRecord(models.Model):
    _name = 'lamgido.dw.record'
    _description = 'DW Fact Record'

    name = fields.Char(string='Label')
    date = fields.Date(required=True, default=fields.Date.context_today)
    category_id = fields.Many2one(
        'lamgido.dw.category',
        string='Category',
        required=True,
    )
    measure_amount = fields.Float(string='Amount', help='Main numeric measure')
    measure_qty = fields.Float(string='Quantity')
    notes = fields.Text()

