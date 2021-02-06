from odoo import api, exceptions, fields, models, _

# class MedinesiaInit(models.TransientModel):

#     _name = "medinesia.init"
#     _columns = {}
#     _defaults = {}

#     @api.model
#     def _init_settings(self):
#         config = self.env['res.config.settings'].create({})
#         config.group_stock_multi_warehouses = True
#         config.group_stock_multi_locations = True
#         config.execute()
#         return True
