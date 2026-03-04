from odoo import models, fields, api


class DwRecordCompute(models.Model):
    _inherit = 'lamgido.dw.record'

    total_value = fields.Float(
        compute='_compute_total_value',
        store=True
    )

    @api.depends('quantity', 'value_per_unit')
    def _compute_total_value(self):
        for rec in self:
            rec.total_value = rec.quantity * rec.value_per_unit