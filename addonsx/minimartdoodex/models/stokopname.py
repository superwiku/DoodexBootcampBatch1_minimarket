from odoo import models, fields, api

class DoodexStokOpname(models.Model):
    _name = 'doodex.stokopname'
    _description = 'doodexStokOpname'
    _rec_name = 'tgl_stokopname'

    tgl_stokopname = fields.Date('tgl_stokopname', default=fields.Date.today())
    detailstokopname_ids = fields.One2many(comodel_name='doodex.detailstokopname', inverse_name='stokopname_id', string='Detail Stok Opname')
    
    


class DoodexDetailStokOpname(models.Model):
    _name = 'doodex.detailstokopname'
    _description = 'DoodexDetailStokOpname'

    name = fields.Char(string='name')
    
    
    barang_id = fields.Many2one(comodel_name='doodex.barang', string='barang')
    stokopname_id = fields.Many2one(comodel_name='doodex.stokopname', string='stokopname')
    check = fields.Boolean(string='Check')
    catatan = fields.Char(string='Catatan')
    
    
    
    
    @api.onchange('barang_id')
    def _compute_name(self):
        rec = self.env['doodex.barang'].search([]).mapped('nama_barang')
        print(rec)
        res={}
        for i in rec:
            res[self.name] = i
    
    
    @api.model
    def default_get(self, name):
        res = super(DoodexDetailStokOpname, self).default_get(name)
        res['barang_id'] = (4, nama_barang) # (4, ID of m2o field)
        return res

    
    
    




    
    
