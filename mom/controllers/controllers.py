# -*- coding: utf-8 -*-
from odoo import http

# class Mom(http.Controller):
#     @http.route('/mom/mom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mom/mom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mom.listing', {
#             'root': '/mom/mom',
#             'objects': http.request.env['mom.mom'].search([]),
#         })

#     @http.route('/mom/mom/objects/<model("mom.mom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mom.object', {
#             'object': obj
#         })