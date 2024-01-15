from odoo import models, fields, api

class DoodexManusiaX(models.Model):
    _inherit = 'res.partner'

    is_manusiax = fields.Boolean(string='apakah manusiax', default=True)
