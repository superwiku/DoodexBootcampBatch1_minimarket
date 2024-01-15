from odoo import models, fields, api

class DoodexManusia(models.Model):
    _name = 'doodex.manusia'
    _description = 'deskripsi global manusia'
    _rec_name = 'nama'

    nama = fields.Char(string='Nama', required=True)
    gender = fields.Selection(string='Gender', selection=[('male', 'Male'), ('female', 'Female'),])
    alamat = fields.Char(string='Alamat')
    
    
    
