from odoo import models, fields, api

class StudentScore(models.Model):
    _name = 'student.management.score'
    _description = 'Score'

    subject = fields.Char(string="Môn học")

    score = fields.Float(string="Điểm")

    note = fields.Text(string="Ghi chú")

    student_id = fields.Many2one(
        'student.management.student',
        string="Sinh Viên"
    )


    @api.onchange('score')
    def _onchange_score(self):

        if not self.score:
            return

        if self.score > 10:
            self.score = 10
            return {
                'warning': {
                    'title': 'Cảnh báo',
                    'message': 'Điểm không được lớn hơn 10'
                }
            }

        if self.score < 4:
            return {
                'warning': {
                    'title': 'Cảnh báo',
                    'message': 'Điểm dưới trung bình'
                }
            }