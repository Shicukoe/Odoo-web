from odoo import models, fields, api

class Student(models.Model):
    _name = 'student.management.student'
    _description = 'Student'

    name = fields.Char(string="Họ tên", required=True)
    student_code = fields.Char(string="Mã Sinh Viên", required=True)

    birth_date = fields.Date(string="Ngày sinh")
    gender = fields.Selection([
        ('male', 'Nam'),
        ('female', 'Nữ')
    ])

    class_id = fields.Many2one(
        'student.management.class',
        string="Lớp"
    )

    score_ids = fields.One2many(
        'student.management.score',
        'student_id',
        string="Danh sách Điểm số"
    )

    gpa = fields.Float(
        string="GPA",
        compute="_compute_gpa",
        store=True
    )

    attachment_ids = fields.Many2many(
        'ir.attachment',
        string="Attachments"
    )

    @api.depends('score_ids.score')
    def _compute_gpa(self):
        for rec in self:
            if rec.score_ids:
                total = sum(rec.score_ids.mapped('score'))
                rec.gpa = total / len(rec.score_ids)
            else:
                rec.gpa = 0