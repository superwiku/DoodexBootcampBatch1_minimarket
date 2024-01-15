from odoo import models, fields, api

class DoodexPelanggan(models.Model):
    _name = 'doodex.pelanggan'
    _inherit = 'doodex.manusia'
    _description = 'model.technical.name'
    _rec_name = 'id_member'

    id_member = fields.Char(string='ID Member')
    tgl_daftar = fields.Date(string='Tanggal Daftar', default=fields.Date.today())
    poin = fields.Integer(string='Poin', readonly=True)  
    penjualan_ids = fields.One2many(comodel_name='doodex.penjualan', inverse_name='pelanggan_id', string='Data Pembelian')
    total_belanja = fields.Integer(compute='_compute_total_belanja', string='total_belanja')
    level = fields.Char(compute='_compute_level', string='Level Member')
    
    @api.onchange('poin')
    def _compute_level(self):
        for rec in self:
            if rec.poin > 500:
                rec.level = 'platinum'
            elif rec.poin > 200:
                rec.level = 'gold'
            else:
                rec.level = 'silver'
    
    @api.depends('penjualan_ids')
    def _compute_total_belanja(self):
        for rec in self:
            a = self.env['doodex.penjualan'].search([('pelanggan_id','=',rec.id)]).mapped('total_bayar')           
            total = sum(a)
            rec.total_belanja = total
            rec.poin = rec.total_belanja // 10000
    
    