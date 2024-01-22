from odoo import models, fields, api
from dateutil.relativedelta import relativedelta

class DoodexEditBarang(models.Model):
    _inherit = 'doodex.barang'
    _description = 'DoodexEditBarang'

    now = fields.Date(string='Now', default=fields.Date.today())
    
    expired_time = fields.Integer(string='Expired Time')
    expired_date = fields.Date(string='Expired Date', compute='_compute_expired_date', inverse='_compute_inverse_expired_date')

    @api.depends('expired_time')
    def _compute_expired_date(self):
        for rec in self:
            rec.expired_date = rec.now + relativedelta(years=rec.expired_time)
    
    @api.depends('expired_date')
    def _compute_inverse_expired_date(self):
        for rec in self:
            rec.expired_time = rec.expired_date.year - rec.now.year
