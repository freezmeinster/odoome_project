# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProjectTask(models.Model):
    _inherit = 'project.task'

    @api.onchange("mom_id")
    def _onchange_mom(self):
        for task in self:
            task.project_id = self.mom_id.project_id
            task.stage_id = self.mom_id.default_stage_id

    mom_id = fields.Many2one('mom.document', string='MoM')

