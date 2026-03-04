from odoo import models
from odoo.exceptions import UserError


class DwRecordWorkflow(models.Model):
    _inherit = 'lamgido.dw.record'

    def action_confirm(self):
        for rec in self:
            if rec.state != 'draft':
                raise UserError("Only Draft records can be confirmed.")
            rec.state = 'confirmed'

    def action_done(self):
        for rec in self:
            if rec.state != 'confirmed':
                raise UserError("Only Confirmed records can be marked Done.")
            rec.state = 'done'

    def action_reset_to_draft(self):
        for rec in self:
            rec.state = 'draft'