# -*- coding: utf-8 -*-

import base64

from odoo import models, fields, api
from odoo.exceptions import UserError


class StudentExam(models.Model):
    _name = 'bi_student_exam.student_exam'
    _description = 'Quan li danh sach thi cua sinh vien'

    name = fields.Char(string= "Tên Kì Thi",required=True)
    student_id = fields.Many2one(
        'bi_student_exam.student',
        string="Sinh Viên"
    )
    exam_date = fields.Date(string= "Ngày thi")
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('sent', 'Sent')], string="Trạng thái", default='draft')
    line_ids = fields.One2many(
        'bi_student_exam.student_exam_line',
        'exam_id',
        string="Danh sách điểm theo môn"
    )
    total_score = fields.Float(string= "Tổng điểm", compute="_compute_total_score", store=True)
    average_score = fields.Float(string= "Điểm trung bình", compute="_compute_average_score", store=True)
    rank = fields.Selection([('giỏi', 'Giỏi'), ('khá', 'Khá'), ('trung bình', 'Trung Bình'), ('yếu', 'Yếu')], string= "Xếp loại", compute="_compute_rank", store=True)
    
    attachment_ids = fields.Many2many(
        'ir.attachment',
        string="Tệp Đính Kèm"
    )
    
    @api.depends('line_ids.score')
    def _compute_total_score(self):
        if not self.line_ids:
            return 
        for record in self:
            record.total_score = sum(line.score for line in record.line_ids)
            
    @api.depends('line_ids.score')
    def _compute_average_score(self):
        if not self.line_ids:
            return
        for record in self:
            if record.line_ids:
                record.average_score = record.total_score / len(record.line_ids)
            else:
                record.average_score = 0.0

    @api.depends('average_score')
    def _compute_rank(self):
        if not self.line_ids:
            return
        for record in self:
            if record.average_score >= 8.0:
                record.rank = 'giỏi'
            elif record.average_score >= 6.5:
                record.rank = 'khá'
            elif record.average_score >= 5.0:
                record.rank = 'trung bình'
            else:
                record.rank = 'yếu'

    def action_confirm(self):
        for record in self:
            if not record.line_ids:
                raise UserError("Không thể xác nhận kì thi khi chưa có điểm nào được nhập.")
            record.state = 'confirmed'
        for record in self:
            if record.state != 'confirmed':
                raise UserError("Chỉ có thể xác nhận kì thi khi đang ở trạng thái Draft.")
            record.state = 'confirmed'

    def action_sent(self):
        for record in self:
            if record.state != 'confirmed':
                raise UserError("Chỉ có thể hoàn thành kì thi khi đã được xác nhận.")
            record.state = 'sent'

    def action_reset_to_draft(self):
        for record in self:
            record.state = 'draft'    

    # action to generate pdf report for student exam 
    def action_view_report(self):
        self.ensure_one()
        return self.env.ref('bi_student_exam.report_pdf_action').report_action(self)
    
    def action_generate_attachment(self):

        for rec in self:

            if not rec.id:
                raise UserError("Please save the record first.")

            content = f"""
                    Exam: {rec.name}
                    Student: {rec.student_id.name}
                    Total Score: {rec.total_score}
                    Average Score: {rec.average_score}
                    Rank: {rec.rank}
                    Generated At: {fields.Datetime.now()}
                    """

            self.env['ir.attachment'].create({
                'name': 'exam_result.txt',
                'type': 'binary',
                'datas': base64.b64encode(content.encode()),
                'res_model': 'bi_student_exam.student_exam',
                'res_id': rec.id,
            })
       
    