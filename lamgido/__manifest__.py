# -*- coding: utf-8 -*-
{
    'name': "DataWarehouse Dashboard",
    'summary': "Internal data warehouse dashboard and reports",
    'description': """
Data warehouse-style dashboard with categories and fact records,
including list, graph and pivot reports for internal analysis.
""",
    'author': "My Company",
    'category': 'Reporting',
    'version': '16.0.1.0.0',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',

        # Category
        'views/dw_category_views.xml',

        # Records (UI + Menu)
        'views/dw_record_views.xml',

        # Reports
        'views/dw_record_report_views.xml',
    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}