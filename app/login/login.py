# Dependencias
from flask import request


# db
from .logica.sesion.manejo import sesion

# Blueprint
from . import login_bp

from .api import validarUsuarioAPI
from .api import registrarUsuarioAPI


@login_bp.route("/login/validarUsuario", methods=["GET"])
def validarUsuario(usuario=None, contrasena=None):
    usuario = request.args.get("usuario")
    contrasena = request.args.get("password")
    resultado = validarUsuarioAPI(usuario, contrasena)
    if resultado.get_json()["valido"] == "si":
        sesion.expirar()
        sesion.crear(usuario)
    return resultado


@login_bp.route("/login/registrarUsuario", methods=["GET"])
def registrarUsuario():
    usuario = request.args.get("usuario")
    contrasena = request.args.get("password")
    resultado = registrarUsuarioAPI(usuario, contrasena)
    return resultado
