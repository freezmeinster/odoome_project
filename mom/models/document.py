# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Document(models.Model):
    _name = 'mom.document'
    _description = 'mom.document'

    def _compute_task_count(self):
        for doc in self:
            doc.task_count = len(doc.task_ids)

    def _get_default_stage(self):
        ICPSudo = self.env['ir.config_parameter'].sudo()
        stage = ICPSudo.get_param('mom.default_stage_id')
        for doc in self:
            stage_id = self.env['project.task.type'].browse(int(stage))
            doc.default_stage_id = stage_id

    name = fields.Char(required=True)
    project_id = fields.Many2one("project.project")
    task_ids = fields.One2many("project.task", 'mom_id', string="Tasks")
    task_count = fields.Integer(string="Tasks", compute="_compute_task_count")
    date_start = fields.Datetime(default=fields.Datetime.now())
    date_end = fields.Datetime(required=True)
    location = fields.Char()
    participant_ids = fields.Many2many("res.partner")
    default_stage_id = fields.Many2one("project.task.type", compute="_get_default_stage")
    body = fields.Text(required=True)
