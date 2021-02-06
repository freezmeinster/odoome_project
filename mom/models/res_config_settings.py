from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    mom_default_stage_id = fields.Many2one("project.task.type",
            string="Default Stage on Mom",
	    config_parameter='mom.default_stage_id', readonly=False)

