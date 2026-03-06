from odoo import models, fields, api
from odoo.exceptions import UserError

class Student(models.Model):
    _name = 'student.management.student'
    _description = 'Student'

    name = fields.Char(string="Họ tên", required=True)
    student_code = fields.Char(string="Mã Sinh Viên", required=True)

    birth_date = fields.Date(string="Ngày sinh")
    gender = fields.Selection([
        ('male', 'Nam'),
        ('female', 'Nữ')
    ], string="Giới tính")

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
        string="Tệp Đính Kèm"
    )

    @api.depends('score_ids.score')
    def _compute_gpa(self):
        for rec in self:
            if rec.score_ids:
                total = sum(rec.score_ids.mapped('score'))
                rec.gpa = total / len(rec.score_ids)
            else:
                rec.gpa = 0
    
    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)

        count = self.search_count([]) + 1
        res['student_code'] = f"SV{count:03d}"

        return res

    def name_get(self):
        result = []
        for rec in self:
            name = f"[{rec.student_code}] {rec.name}"
            result.append((rec.id, name))
        return result
    
    def unlink(self):
        if not self.env.user.has_group(
            'student_management.group_teacher'
        ):
            raise UserError("Chỉ giáo viên mới được phép xóa sinh viên")
        return super().unlink()

    def check_low_gpa(self):
        students = self.search([('gpa', '<', 4)])

        template = self.env.ref('student_management.email_template_gpa_warning')

        for student in students:
            template.with_context(
                student_name=student.name,
                student_gpa=student.gpa
            ).send_mail(student.id, force_send=True)

    def action_open_report_wizard(self):

        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Student Report',
            'res_model': 'student.report.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_student_id': self.id
            }
        }