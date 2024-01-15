from odoo import models, fields, api

class DoodexBarang(models.Model):
    _name = 'doodex.barang'
    _description = 'ini model barang'
    _rec_name = 'nama_barang'
    
    name = fields.Char(string='Name')
    nama_barang = fields.Char(string='Nama Barang')
    harga = fields.Integer(string='Harga')
    stok = fields.Integer(string='Stok', readonly=True)    
    deskripsi = fields.Char(string='Deskripsi Barang')
    jenis = fields.Many2one(comodel_name='doodex.jenisbarang', string='Kelompok Barang')
    supplier_ids = fields.Many2many(comodel_name='doodex.supplier', string='Supplier')
    harga_modal = fields.Integer(string='Harga Modal')
    
    
    
    
    
    
