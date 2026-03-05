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