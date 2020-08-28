# Dependencias
from flask import request
from app.api import api_bp

from app.api.modelos import Materia
from app.api.modelos import db


@api_bp.route("/api/dashboard/crear_materia", methods=["GET"])
def APIcrearMateria(nombre=None, url=None):
    nombre = request.args.get("nombre")
    url = request.args.get("url")
    alias = request.args.get("alias")
    ma = Materia(nombre, url, alias)
    ma.guardar()
    return {"materia": nombre, "url": url, "alias": alias}
    """
    resultado = validarUsuarioAPI(usuario, contrasena)
    if resultado.get_json()["valido"] == "si":
        expirar()
        crear(usuario)
    return resultado
    """
