# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StudentExamLine(models.Model):
    _name = 'bi_student_exam.student_exam_line'
    _description = 'Danh sách điểm theo môn của sinh viên'

    exam_id = fields.Many2one(
        'bi_student_exam.student_exam',
        string="Kì Thi"
    )
    subject_name = fields.Char(string= "Tên môn học", required=True)
    score = fields.Float(string= "Điểm", digits=(10, 2))
    note = fields.Text(string= "Ghi chú")
