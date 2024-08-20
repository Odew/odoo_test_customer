# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Test ODW',
    'version': '1.0.0.0.1',
    'category': 'Other',
    'summary': 'Test ODW Module',
    'description': """This is a test module""",
    'depends': ["base", "sale", "purchase"],
    'data': [
        "views/res_partner_views.xml",
    ],
    'installable': True,
    'license': 'LGPL-3',
}

