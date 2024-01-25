from odoo import models, fields, api
from dateutil.relativedelta import relativedelta

class EditSaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'EditSaleOrder'

    validity_datex = fields.Datetime(compute='_compute_validity_date', string='Expirationx')
    xxx = fields.Char(string='XXX')
    
    
    @api.depends('date_order')
    def _compute_validity_date(self):
        for rec in self:
            rec.validity_datex  = rec.date_order  + relativedelta(months=1,days=3)
