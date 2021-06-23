from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS

import Master

#from Master.Pengguna import FormPengguna, TabelPengguna
#from Master.Pelanggan import FormPelanggan, TabelPelanggan
#from Master.Barang import FormBarang, TabelBarang, DataBarang
#from Master.Supplier import FormSupplier, TabelSupplier
#from Pembelian.form import FormPembelian, TabelPembelian
#from Class.Main import Order
#from Pengaturan.Satuan import FormSatuan, TabelSatuan
#from Pengaturan.Kategori import FormKategori, TabelKategori
#from Pengaturan.Merek import FormMerek, TabelMerek

app = Flask(__name__)
api = Api(app)

CORS(app)
cors = CORS(app, resources = {r"/*" : { "origin" : "*" }})
"""
# Master Data [Barang]
api.add_resource(FormBarang, "/master/barang/form/<string:id>");
api.add_resource(TabelBarang, "/master/barang/tabel")
api.add_resource(DataBarang, "/master/barang/data/<string:id>")

# Master Data [Supplier]
api.add_resource(FormSupplier, "/master/supplier/form/<string:id>");
api.add_resource(TabelSupplier, "/master/supplier/tabel")

# Master Data [Pelanggan]
api.add_resource(FormPelanggan, "/master/pelanggan/form/<string:id>");
api.add_resource(TabelPelanggan, "/master/pelanggan/tabel")

# Master Data [Pengguna]
api.add_resource(FormPengguna, "/master/pengguna/form/<string:id>");
api.add_resource(TabelPengguna, "/master/pengguna/tabel")

# Pembelian
api.add_resource(FormPembelian, "/pembelian/order/<string:id>");
api.add_resource(TabelPembelian, "/pembelian")

# Order for Handling [PEMBELIAN] and PENJUALAN
#api.add_resource(Order, "/orders/<string:id>")

api.add_resource(Order, '/orders/<string:type>', methods=["GET"], endpoint="orders")
api.add_resource(Order, '/order/<string:id>', methods=["GET", "POST"], endpoint="orderGet")

# Pengaturan [Satuan]
api.add_resource(FormSatuan, "/pengaturan/satuan/form/<string:id>");
api.add_resource(TabelSatuan, "/pengaturan/satuan/tabel")

# Pengaturan [Kategori]
api.add_resource(FormKategori, "/pengaturan/kategori/form/<string:id>");
api.add_resource(TabelKategori, "/pengaturan/kategori/tabel")

# Pengaturan [Merek]
api.add_resource(FormMerek, "/pengaturan/merek/form/<string:id>");
api.add_resource(TabelMerek, "/pengaturan/merek/tabel")

###### Environment for Version 2 ###########################
from Class.Main import Barang

# Master Barang

api.add_resource(Barang, '/barang', methods=["GET", "POST"], endpoint="barang")
api.add_resource(Barang, '/barang/<string:onlyActive>', methods=["GET", "POST"], endpoint="barangOnlyActive")
api.add_resource(Barang, '/barang/id/<string:id>', methods=["GET","POST","DELETE"], endpoint="barangById")
"""

# Register to The Components
routes = [Master]
for route in routes:
   route.register(api)

if __name__ == "__main__":
   app.run(debug=True, host="0.0.0.0")
