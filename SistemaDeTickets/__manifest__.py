# -*- coding: utf-8 -*-

{
    'name': 'Sistema de Tickets',
    'summary': 'Gestión de tickets para el área de sistemas',
    'author': 'Sergio Martinez Meneses',
    'category': 'Herramientas',
    'version': '1.0.0',
    'description': """
        Este módulo permite gestionar los tickets del área de sistemas, 
        facilitando la creación, seguimiento y cierre de tickets.
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/ticket_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
