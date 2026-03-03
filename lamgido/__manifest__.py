# -*- coding: utf-8 -*-
{
    'name': "DataWarehouse_Dashboard",
    'summary': "Internal data warehouse dashboard and reports",
    'description': """
Data warehouse-style dashboard with categories and fact records,
including list, graph and pivot reports for internal analysis.
""",
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Reporting',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'demo': [],
}