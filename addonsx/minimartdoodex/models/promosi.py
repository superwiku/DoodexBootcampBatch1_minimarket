from odoo import models, fields, api

class DoodexPromosi(models.Model):
    _inherit = 'res.partner'

    is_promosi = fields.Boolean(string='is Promosi', default=False)