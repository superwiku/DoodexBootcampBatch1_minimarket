from odoo import http, models, fields
from odoo.http import request
import json

class MinimartDoodexHttp(http.Controller):
    @http.route('/api/getbarang', auth='public', method=['GET'])
    def getBarang(self, **kw):
        barang = request.env['doodex.barang'].search([])
        isi = []
        for b in barang:
            isi.append({
                'namabarang' : b.nama_barang,
                'modal' : b.harga_modal,
                'jual' : b.harga,
                'stok' : b.stok
            })
        return json.dumps(isi)
    