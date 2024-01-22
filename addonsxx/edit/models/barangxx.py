from odoo import models, fields, api

class DoodexEditBarangxx(models.Model):
    _name = 'doodexedit.barang'
    _description = 'DoodexEditBarangxx'
    _rec_name = 'nama_edit'

    barang_id = fields.Many2one(comodel_name='doodex.barang', string='Nama Barang')
    # barang = fields.Char(string='Nama Barang')
    
    nama_edit = fields.Char(compute='_compute_nama_edit', string='Nama Barang Edit')
    
    @api.depends('barang_id')
    def _compute_nama_edit(self):
        for rec in self:
            rec.nama_edit = str(rec.barang_id.nama_barang) + " hasil edit"