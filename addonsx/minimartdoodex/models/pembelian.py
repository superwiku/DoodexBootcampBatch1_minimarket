from odoo import models, fields, api, _

class DoodexPembelian(models.Model):
    _name = 'doodex.pembelian'
    _description = 'model.technical.name'
    name = fields.Char(string='Kode Pembelian')
    barang_id = fields.Many2one(comodel_name='doodex.barang', string='Nama Barang')
    supplier_id = fields.Many2one(comodel_name='doodex.supplier', string='Supplier')
    qty_beli = fields.Integer(string='Quantiy Pembelian')
    modal = fields.Char(compute='_compute_modal', string='Harga Beli')
    bayar = fields.Char(compute='_compute_bayar', string='bayar')
    
    @api.depends('barang_id')
    def _compute_modal(self):
        for rec in self:
            rec.modal = rec.barang_id.harga_modal
 
    @api.depends('barang_id', 'qty_beli')
    def _compute_bayar(self):
        for rec in self:
            rec.bayar = rec.barang_id.harga_modal * rec.qty_beli
    
    @api.model
    def create(self,vals):           
        record = super(DoodexPembelian, self).create(vals)      
        if record.qty_beli: 
            self.env['doodex.barang'].search([('id','=',record.barang_id.id)]).write({'stok' : record.barang_id.stok + record.qty_beli})
        return record

    def unlink(self):
        for r in self:
            r.barang_id.stok -= r.qty_beli
        record = super(DoodexPembelian, self).unlink()
    
    @api.onchange('barang_id')
    def _onchange_barang(self):
        a = self.barang_id.supplier_ids
        b = []
        for i in a:            
            b.append(i.id)
        return {'domain':{'supplier_id':[('id','in',b)]}}

 