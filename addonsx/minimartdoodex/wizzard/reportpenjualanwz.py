from odoo import models, fields, api

class ReportPenjualanWz(models.TransientModel):
    _name = 'doodex.reportpenjualanwz'
    _description = 'model.technical.name'

    dari_tgl = fields.Date(string='dari Tanggal', required=True)
    ke_tgl = fields.Date(string='ke Tanggal', required=True)
    penjualan_id = fields.Many2one(comodel_name='doodex.penjualan', string='')
    

    def action_penjualan_report(self):
        laporan = []
        dari = self.dari_tgl
        ke = self.ke_tgl
        if dari:
            laporan += [('tgl_transaksi','>=', dari)]
        if ke:
            laporan += [('tgl_transaksi','<=', ke)]
        print(laporan)
        laporan_jadi = self.env['doodex.penjualan'].search_read(laporan)
        
        data = {
            'form' : self.read()[0],
            'laporannya' : laporan_jadi            
        }
        report_action = self.env.ref('minimartdoodex.report_penjualan_wizard').report_action(self, data=data)
        report_action['close_on_report_download'] = True
        return report_action