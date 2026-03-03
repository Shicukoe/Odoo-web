# -*- coding: utf-8 -*-
{
    'name': "DataWarehouse_Dashboard",
    'summary': "Internal data warehouse dashboard and reports",
    'description': """
Data warehouse-style dashboard with categories and fact records,
including list, graph and pivot reports for internal analysis.
""",
    'author': "My Company",
    'category': 'Reporting',
    'version': '16.0.1.0.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'demo': [],
    'application': True,
    'installable': True,
}