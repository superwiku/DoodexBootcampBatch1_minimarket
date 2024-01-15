# -*- coding: utf-8 -*-
# from odoo import http


# class Minimartdoodex(http.Controller):
#     @http.route('/minimartdoodex/minimartdoodex', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/minimartdoodex/minimartdoodex/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('minimartdoodex.listing', {
#             'root': '/minimartdoodex/minimartdoodex',
#             'objects': http.request.env['minimartdoodex.minimartdoodex'].search([]),
#         })

#     @http.route('/minimartdoodex/minimartdoodex/objects/<model("minimartdoodex.minimartdoodex"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('minimartdoodex.object', {
#             'object': obj
#         })

