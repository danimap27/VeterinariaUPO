# -*- coding: utf-8 -*-
# from odoo import http


# class VeterinariaUpo(http.Controller):
#     @http.route('/veterinaria_upo/veterinaria_upo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/veterinaria_upo/veterinaria_upo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('veterinaria_upo.listing', {
#             'root': '/veterinaria_upo/veterinaria_upo',
#             'objects': http.request.env['veterinaria_upo.veterinaria_upo'].search([]),
#         })

#     @http.route('/veterinaria_upo/veterinaria_upo/objects/<model("veterinaria_upo.veterinaria_upo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('veterinaria_upo.object', {
#             'object': obj
#         })
