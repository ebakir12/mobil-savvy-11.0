# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Custom Categories Horizontal',
    'version': '1.0',
    'category': 'Custom',
    'depends': ['website_sale'],
    'description': """
This is Custom display for eCommerce Categories in Odoo.
========================================================================

Products support categories and this allows the user to filter the list of Products
based on the category selected
    """,
    'data': [
        'views/product_categories_views.xml'
    ],
    'installable': True,
    'auto_install': False,
}
