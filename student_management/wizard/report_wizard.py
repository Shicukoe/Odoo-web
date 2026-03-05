from odoo import models, fields


class StudentReportWizard(models.TransientModel):
    _name = 'student.report.wizard'

    student_id = fields.Many2one(
        'student.management.student',
        string="Sinh Viên"
    )

    date_from = fields.Date(string="From Date")
    date_to = fields.Date(string="To Date")

    def action_print_report(self):

        data = {
            'student_id': self.student_id.id,
            'date_from': self.date_from,
            'date_to': self.date_to,
        }

        return self.env.ref(
            'student_management.student_report_action'
        ).report_action(self, data=data)