# -*- coding: utf-8 -*-
# from odoo import http


# class BiStudentExam(http.Controller):
#     @http.route('/bi_student_exam/bi_student_exam', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bi_student_exam/bi_student_exam/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bi_student_exam.listing', {
#             'root': '/bi_student_exam/bi_student_exam',
#             'objects': http.request.env['bi_student_exam.bi_student_exam'].search([]),
#         })

#     @http.route('/bi_student_exam/bi_student_exam/objects/<model("bi_student_exam.bi_student_exam"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bi_student_exam.object', {
#             'object': obj
#         })
