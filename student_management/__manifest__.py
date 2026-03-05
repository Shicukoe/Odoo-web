{
    'name': 'Student Management',
    'version': '1.0',
    'depends': ['base', 'mail'],
    'data': [
        'security/student_security.xml',
        'security/ir.model.access.csv',

        'views/student_views.xml',
        'views/class_views.xml',
        'views/score_views.xml',
        'views/kanban_views.xml',

        'views/menu.xml',

        'wizard/report_wizard_view.xml',

        'report/report_action.xml',
        'report/student_report_template.xml',

        'data/cron_job.xml',
        'data/email_template.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'student_management/static/src/js/gpa_widget.js',
            'student_management/static/src/xml/gpa_widget_template.xml',
        ],
    },
}