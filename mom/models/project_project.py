# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProjectProject(models.Model):
    _inherit = 'project.project'

    def _compute_mom_count(self):
        for project in self:
            project.mom_count = len(self.mom_ids)

    mom_count = fields.Integer(compute='_compute_mom_count', string="MoM Count")
    mom_ids = fields.One2many('mom.document', 'project_id', string='MoM')

