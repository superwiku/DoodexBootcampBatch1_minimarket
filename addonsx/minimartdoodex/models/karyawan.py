from odoo import models, fields, api

class DoodexKaryawan(models.Model):
    _name = 'doodex.karyawan'    
    _inherit = 'doodex.manusia'    
    _description = 'doodex.karyawan'
    _rec_name = 'id_karyawan'
 
    id_karyawan = fields.Char(string='ID Karyawan')
    bagian = fields.Selection(string='Bagian', 
                              selection=[('kasir', 'Kasir'), 
                                         ('akunting', 'Akunting'), 
                                         ('kebersihan', 'Kebersihan'),], 
                              required=True)
    gaji = fields.Integer(string='Gaji per bulan')
    foto = fields.Binary(string='Foto')
    
    

class DoodexKaryawanBaru(models.Model):
    _inherit = 'doodex.karyawan'
    is_baru = fields.Boolean(string='Baru', default=False)
    

    
    
    