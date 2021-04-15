# -*- coding: utf-8 -*-

{
    'name': 'Point of sale extend',
    'version': '13.0.1.1.0',
    'category': 'Point de vente',
    'summary': """
        Point of sale
    """,
    'description': """Point of sale""",
    'author': 'Leansoft',
    'company': 'Leansoft',
    'maintainer': 'Leansoft',
    'website': 'www.leansoft.ma',
    'depends': ['point_of_sale'],
    'data': [
        'security/ir.model.access.csv',
        'reports/control.xml',
        'views/pos.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'AGPL-3',
}