# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Document(models.Model):
    _name = 'mom.document'
    _description = 'mom.document'

    name = fields.Char()
    project_id = fields.Many2one("project.project")
    date = fields.Date()
    participant_ids = fields.Many2many("res.partner")
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
    body = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
