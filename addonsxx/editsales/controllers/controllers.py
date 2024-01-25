# -*- coding: utf-8 -*-
# from odoo import http


# class Editsales(http.Controller):
#     @http.route('/editsales/editsales', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/editsales/editsales/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('editsales.listing', {
#             'root': '/editsales/editsales',
#             'objects': http.request.env['editsales.editsales'].search([]),
#         })

#     @http.route('/editsales/editsales/objects/<model("editsales.editsales"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('editsales.object', {
#             'object': obj
#         })
