from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS

from Master.Barang import FormBarang, TabelBarang

app = Flask(__name__)
api = Api(app)

CORS(app)
cors = CORS(app, resources = {
		r"/*" : { "origin" : "*" }
	   })

api.add_resource(FormBarang, "/master/barang/form/<string:id>");
api.add_resource(TabelBarang, "/master/barang/tabel")

if __name__ == "__main__":
   app.run(debug=True, host="0.0.0.0")
