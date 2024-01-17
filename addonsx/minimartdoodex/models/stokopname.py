from odoo import models, fields, api

class DoodexStokOpname(models.Model):
    _name = 'doodex.stokopname'
    _description = 'doodexStokOpname'
    _rec_name = 'tgl_stokopname'

    tgl_stokopname = fields.Date('tgl_stokopname', default=fields.Date.today())
    detailstokopname_ids = fields.One2many(comodel_name='doodex.detailstokopname', inverse_name='stokopname_id', string='Detail Stok Opname')
    
    @api.model
    def default_get(self, fields):
        res = super(DoodexStokOpname, self).default_get(fields)
        barang_record = self.env['doodex.barang'].search([])
        detail_vals = []
        for i in barang_record:
            detail_vals.append((0,0,{
                'barang_id': i.id,
                'check' : False,
                'catatan' : ''
            }))
        res['detailstokopname_ids'] = detail_vals
        return res


class DoodexDetailStokOpname(models.Model):
    _name = 'doodex.detailstokopname'
    _description = 'DoodexDetailStokOpname'

    name = fields.Char(compute='_compute_name',string="name")
    stok = fields.Integer(compute='_compute_stok', string='Stok')
    barang_id = fields.Many2one(comodel_name='doodex.barang', string='barang')
    stokopname_id = fields.Many2one(comodel_name='doodex.stokopname', string='stokopname')
    check = fields.Boolean(string='Check')
    catatan = fields.Char(string='Catatan')
    
    @api.depends('barang_id')
    def _compute_name(self):
        for rec in self:
            rec.name = rec.barang_id.nama_barang
    
    @api.depends('barang_id')
    def _compute_stok(self):
        for re in self:
            re.stok = re.barang_id.stok


    
    
    




    
    
