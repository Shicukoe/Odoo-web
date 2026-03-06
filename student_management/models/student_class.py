from odoo import models, fields

class StudentClass(models.Model):
    _name = 'student.management.class'
    _description = 'Class'

    name = fields.Char(string="Tên Lớp", required=True)

    teacher_id = fields.Many2one(
        'res.users',
        string="Giáo Viên"
    )

    student_ids = fields.One2many(
        'student.management.student',
        'class_id',
        string="Sinh Viên"
    )

    student_count = fields.Integer(
        string="Số lượng Sinh Viên",
        compute="_compute_student_count"
    )

    def _compute_student_count(self):

        for rec in self:
            rec.student_count = self.env[
                'student.management.student'
            ].search_count([
                ('class_id', '=', rec.id)
            ])