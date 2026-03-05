from odoo import models, fields, api

class StudentScore(models.Model):
    _name = 'student.management.score'
    _description = 'Score'

    subject = fields.Char()

    score = fields.Float()

    note = fields.Text()

    student_id = fields.Many2one(
        'student.management.student'
    )

    @api.onchange('score')
    def _onchange_score(self):
        if self.score > 10:
            self.score = 10
            return {
                'warning': {
                    'title': 'Warning',
                    'message': 'Điểm khong được vượt quá 10'
                }
            }

        if self.score < 4:
            return {
                'warning': {
                    'title': 'Warning',
                    'message': 'Điểm dưới trung bình'
                }
            }