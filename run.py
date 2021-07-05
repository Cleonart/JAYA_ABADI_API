#!/usr/bin/env python3

from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS

import Master
import Order

#from Pengaturan.Satuan import FormSatuan, TabelSatuan
#from Pengaturan.Kategori import FormKategori, TabelKategori
#from Pengaturan.Merek import FormMerek, TabelMerek

app = Flask(__name__)
api = Api(app)

CORS(app)
cors = CORS(app, resources = {r"/*" : { "origin" : "*" }})
"""
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

"""

# Register Components and Modules
routes = [Master, Order]
for route in routes:
   route.register(api)

if __name__ == "__main__":
   app.run(debug=True, host="0.0.0.0")
