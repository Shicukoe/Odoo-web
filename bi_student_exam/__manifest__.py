# -*- coding: utf-8 -*-
{
    'name': "bi_student_exam",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        #security
        # 'security/ir.model.access.csv',

        #views
        'views/students_exam_views.xml',
        'views/exam_results_views.xml',
        'views/menu.xml',

        #reports
        'report/report_action.xml',
        'report/report_pdf_template.xml',
        #email templates

        
        #widgets

    ],
    # 'assets': {
    # 	'web.assets_backend': [
    #     	'one2many_mass_select_delete/static/src/js/widget.js',
    # 	],
    # 	'web.assets_qweb': [
    #     	'one2many_mass_select_delete/static/src/xml/widget_view.xml',
    # 	],
	# },
}
