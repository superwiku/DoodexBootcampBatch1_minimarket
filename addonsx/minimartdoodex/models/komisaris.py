from odoo import models, fields, api

class DoodexKomisaris(models.Model):
    _inherit = 'res.partner'

    gaji = fields.Integer(string='Gaji')
    
