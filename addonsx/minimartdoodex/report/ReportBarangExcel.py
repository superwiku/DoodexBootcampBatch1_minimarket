from odoo import models, fields, api

class DaftarBarangXlsx(models.AbstractModel):
    _name = 'report.minimartdoodex.report_barang_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    tgl_laporan = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, barang):
        sheet = workbook.add_worksheet('Daftar Barang')
        bold = workbook.add_format({'bold': True})
        italic = workbook.add_format({'italic': True})
        row = 1
        col = 0
        sheet.write(0, 0, str(self.tgl_laporan))
        sheet.write(row, col, 'Nama Barang', bold)
        sheet.write(row, col+1, 'Harga', bold)
        sheet.write(row, col+2, 'Stok', bold)
        sheet.write(row, col+3, 'Supplier', bold)
        for obj in barang:
            row += 1
            col = 0
            sheet.write(row, col, obj.nama_barang, italic)
            sheet.write(row, col+1, obj.harga)
            sheet.write(row, col+2, obj.stok)
            for i in obj.supplier_ids:
                sheet.write(row, col+3, i.name, italic)
                col+=1
            