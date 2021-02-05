# -*- coding: utf-8 -*-
{
    'name': "Minute of Meeting",

    'summary': """ Minute of Meeting """,
    'description': """ Minute of Meeting """,

    'author': "Bramandityo Prabowo",
    'website': "https://mula.cloud",

    'category': 'Utility',
    'version': '0.0.1',

    'application': True,

    'depends': ['base', 'project'],

    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/project_project.xml',
        'views/document.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
