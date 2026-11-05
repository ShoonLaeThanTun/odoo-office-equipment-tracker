
{
    'name': 'Office Equipment Tracker',
    'version': '18.0.1.0.0',
    'category': 'Operations',
    'summary': 'Manage company equipment and employee assignments',
    'description': """
        A simple equipment management application.
        Track equipment, employee assignments,
        due dates, and equipment availability.
    """,
    'author': 'Shoon Lae Than Tun',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/equipment_views.xml',
    ],
    'installable': True,
    'application': True,
}
