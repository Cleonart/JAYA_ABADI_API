from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS

from Master.Barang import FormBarang, TabelBarang
from Master.Pengguna import FormPengguna, TabelPengguna
from Master.Pelanggan import FormPelanggan, TabelPelanggan
from Master.Supplier import FormSupplier, TabelSupplier
from Pembelian.form import FormPembelian
from Pengaturan.Satuan import FormSatuan, TabelSatuan
from Pengaturan.Kategori import FormKategori, TabelKategori
from Pengaturan.Merek import FormMerek, TabelMerek

app = Flask(__name__)
api = Api(app)

CORS(app)
cors = CORS(app, resources = {
		r"/*" : { "origin" : "*" }
	   })

# Master Data [Barang]
api.add_resource(FormBarang, "/master/barang/form/<string:id>");
api.add_resource(TabelBarang, "/master/barang/tabel")

# Master Data [Supplier]
api.add_resource(FormSupplier, "/master/supplier/form/<string:id>");
api.add_resource(TabelSupplier, "/master/supplier/tabel")

# Master Data [Pelanggan]
api.add_resource(FormPelanggan, "/master/pelanggan/form/<string:id>");
api.add_resource(TabelPelanggan, "/master/pelanggan/tabel")

# Master Data [Pengguna]
api.add_resource(FormPengguna, "/master/pengguna/form/<string:id>");
api.add_resource(TabelPengguna, "/master/pengguna/tabel")

# Pengaturan [Satuan]
api.add_resource(FormPembelian, "/pembelian/order/<string:id>");

# Pengaturan [Satuan]
api.add_resource(FormSatuan, "/pengaturan/satuan/form/<string:id>");
api.add_resource(TabelSatuan, "/pengaturan/satuan/tabel")

# Pengaturan [Kategori]
api.add_resource(FormKategori, "/pengaturan/kategori/form/<string:id>");
api.add_resource(TabelKategori, "/pengaturan/kategori/tabel")

# Pengaturan [Merek]
api.add_resource(FormMerek, "/pengaturan/merek/form/<string:id>");
api.add_resource(TabelMerek, "/pengaturan/merek/tabel")

if __name__ == "__main__":
   app.run(debug=True, host="0.0.0.0")
