# -*- coding: utf-8 -*-
# from odoo import http


# class Edit(http.Controller):
#     @http.route('/edit/edit', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/edit/edit/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('edit.listing', {
#             'root': '/edit/edit',
#             'objects': http.request.env['edit.edit'].search([]),
#         })

#     @http.route('/edit/edit/objects/<model("edit.edit"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('edit.object', {
#             'object': obj
#         })
