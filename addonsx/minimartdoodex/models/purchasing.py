from odoo import models, fields, api

class DoodexPurchasing(models.Model):
    _inherit = 'res.partner'

    is_purchasing = fields.Boolean(string='is Purchasing', default=False)
    
