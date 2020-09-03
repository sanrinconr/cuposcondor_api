from flask_restful import Resource
from .logica import Materia, Materias, Cupo
from flask import request


class MateriaApi(Resource):
    def post(self):
        body = request.get_json()
        return Materia.agregar(body)

    def get(self):
        id_materia = request.args.get("id_materia")
        return Materia.obtener(id_materia)


class MateriasApi(Resource):
    def get(self):
        return Materias.obtener()


class CupoApi(Resource):
    def get(self):
        id_materia = request.args.get("id_materia")
        return Cupo.buscar(id_materia)
