from flask_restful import Resource
from .logica import Materia, Materias, Cupo
from flask import request


class MateriaApi(Resource):
    def put(self):
        body = request.get_json(force=True)
        return Materia.agregar(body)

    def get(self):
        id_materia = request.args.get("id_materia")
        return Materia.obtener(id_materia)

    def delete(self):
        body = request.get_json(force=True)
        return Materia.eliminar(body)


class MateriasApi(Resource):
    def get(self):
        return Materias.obtener()


class CupoApi(Resource):
    def get(self):
        id_materia = request.args.get("id_materia")
        return Cupo.buscar(id_materia)
