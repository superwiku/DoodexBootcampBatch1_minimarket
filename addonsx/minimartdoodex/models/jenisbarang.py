from odoo import models, fields, api

class DoodexJenisBarang(models.Model):
    _name = 'doodex.jenisbarang'
    _description = 'model.technical.name'
    _rec_name = 'nama'

    nama = fields.Selection(string='Jenis', selection=[('detergen', 'Detergen'), ('bahanmakanan', 'Bahan Makanan'),('makanankering', 'Makanan Kering'),('buah', 'Buah'),])
        
    letak = fields.Char(string='No. Rak')
    daftarbarang = fields.One2many(comodel_name='doodex.barang', inverse_name='jenis', string='Daftar Barang')
           
    kode = fields.Char(string='Kode')

    @api.onchange('nama','letak')
    def _onchange_kode(self):
        if self.nama == 'detergen':
            self.kode = 'dt'+str(self.letak) 
        elif self.nama == 'bahanmakanan':
            self.kode = 'bm'+str(self.letak) 
        elif self.nama == 'makanankering':
            self.kode = 'mk'+str(self.letak) 
    
    
   