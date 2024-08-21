# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Odoo Space App',
    'version': '0.1',
    'summary': 'App to track and manage Spaceships',
    'author': 'Odoo',
    'website': 'odoo.com',
    'category': 'Parent Category/Category',
    'license': 'OPL-1',

    'depends': [
        'base',
        'contacts',
        'sale',
    ],
    'data': [
        'views/menuitems.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
}