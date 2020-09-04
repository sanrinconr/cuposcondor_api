from flask import Blueprint, jsonify
from app import api, jwt
from .consultas import MateriaApi, CupoApi, MateriasApi

# El blueprint api
dashboard_bp = Blueprint("dashboard", __name__)

api.add_resource(MateriaApi, "/api/materia/")
api.add_resource(MateriasApi, "/api/materias/")
api.add_resource(CupoApi, "/api/cupos/buscar/")

# CUSTOMIZACION DE ERRORES RESPECTO A LOS TOKENS
@jwt.expired_token_loader
def callback_token_expirado(expired_token):
    return (
        jsonify(
            {
                "status": 401,
                "sub_status": 42,
                "msg": "El token de acceso a expirado, realizar login",
            }
        ),
        401,
    )


@jwt.unauthorized_loader
def callback_token_no_enviado(self):
    return (
        jsonify(
            {
                "status": 401,
                "sub_status": 42,
                "msg": "No se envio token de acceso, realizar login",
            }
        ),
        401,
    )
