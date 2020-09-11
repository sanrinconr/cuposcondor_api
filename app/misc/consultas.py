from flask_restful import Resource
from flask import request
from flask import jsonify


class Misc(Resource):
    def get(self):
        return jsonify({"Exito": True, "Msg": "La conexion fue exitosa!"})
