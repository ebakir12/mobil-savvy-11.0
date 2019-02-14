# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http

class DisplayProductCategories(http.Controller):

    @http.route('/shop/category/<category_link>', auth='public')
    def show_product_categories(self, category_link)
        category_id=category_link.split('-')
        category=http.request.env['product.public.category'].sudo().search([])
        return http.request.render('custom_categories.product_categories_views', 
            {categories: category,
             categoryLink:category_link})