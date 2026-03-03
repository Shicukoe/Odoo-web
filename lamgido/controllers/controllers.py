# -*- coding: utf-8 -*-
# from odoo import http


# class Lamgido(http.Controller):
#     @http.route('/lamgido/lamgido', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lamgido/lamgido/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('lamgido.listing', {
#             'root': '/lamgido/lamgido',
#             'objects': http.request.env['lamgido.lamgido'].search([]),
#         })

#     @http.route('/lamgido/lamgido/objects/<model("lamgido.lamgido"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lamgido.object', {
#             'object': obj
#         })
