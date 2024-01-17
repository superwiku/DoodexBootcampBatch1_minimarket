from odoo import models, fields, api, _

class DoodexKaryawan(models.Model):
    _name = 'doodex.karyawan'    
    _inherit = 'doodex.manusia'    
    _description = 'doodex.karyawan'
    _rec_name = 'ref'

    ref = fields.Char(
        string="No. Reference",
        required=True, copy=False, readonly=True,
        default=lambda self: _('New')) 

    bagian = fields.Selection(string='Bagian', 
                              selection=[('kasir', 'Kasir'), 
                                         ('akunting', 'Akunting'), 
                                         ('kebersihan', 'Kebersihan'),], 
                              required=True)
    gaji = fields.Integer(string='Gaji per bulan')
    foto = fields.Binary(string='Foto')
    
    @api.model
    def create(self,vals):
        print(vals)
        if vals.get('ref', _("New")) == _("New"):   
            bag = vals.get('bagian','kasir')
            if bag == 'kasir':
                vals['ref'] = self.env['ir.sequence'].next_by_code('referensi.karyawankasir') or _("New")
            elif bag == 'akunting':
                vals['ref'] = self.env['ir.sequence'].next_by_code('referensi.karyawanakunting') or _("New") 
            elif bag == 'kebersihan':
                vals['ref'] = self.env['ir.sequence'].next_by_code('referensi.karyawankebersihan') or _("New")  
        record = super(DoodexKaryawan, self).create(vals)
        return record

    def write(self,vals):
        bag = vals.get('bagian','kasir')
        if bag == 'kasir':
                vals['ref'] = self.env['ir.sequence'].next_by_code('referensi.karyawankasir') or _("New")
        elif bag == 'akunting':
                vals['ref'] = self.env['ir.sequence'].next_by_code('referensi.karyawanakunting') or _("New") 
        elif bag == 'kebersihan':
                vals['ref'] = self.env['ir.sequence'].next_by_code('referensi.karyawankebersihan') or _("New")  
        record = super(DoodexKaryawan, self).write(vals)
        return record


    
    
    