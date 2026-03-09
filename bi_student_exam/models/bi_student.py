# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Student(models.Model):
    _name = 'bi_student_exam.student'
    _description = 'Danh sach sinh vien'

    student_code = fields.Char(string= "Mã Sinh Viên", required=True)
    name = fields.Char(string= "Họ tên", required=True)
    class_name = fields.Char(string= "Lớp", required=True)
    date_of_birth = fields.Date(string= "Ngày sinh")
    phone = fields.Char(string= "Số điện thoại")
    email = fields.Char(string= "Email")
    guardian_name = fields.Char(string= "Tên người giám hộ", required=True)
    guardian_email = fields.Char(string= "Email người giám hộ", required=True)
