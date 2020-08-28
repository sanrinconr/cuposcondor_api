# Dependencias
from flask import request


# db
from .logica.usuario.inicioSesion import inicioSesion
from .logica.usuario.registro import registro

# Blueprint
from . import login_bp

"""
@login_bp.route("/api/validarUsuario", methods=["GET"])
def validarUsuarioAPI(usuario=None, contrasena=None):
    if request.method == "GET":
        usuario = request.args.get("usuario")
        contrasena = request.args.get("password")
    resultado = inicioSesion.validarExistencia(usuario, contrasena)
    return resultado


@login_bp.route("/api/registrarUsuario", methods=["GET"])
def registrarUsuarioAPI(usuario=None, contrasena=None):
    if request.method == "GET":
        usuario = request.args.get("usuario")
        contrasena = request.args.get("password")
    resultado = registro.agregarUsuario(usuario, contrasena)
    return resultado
"""
