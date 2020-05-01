# Dependencias
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import url_for

# db
from .data.login.inicioSesion import inicioSesion
from .data.login.registro import registro

# Blueprint
from . import login_bp


@login_bp.route("/api/validarUsuario", methods=["GET"])
def validarUsuario():
    usuario = request.args.get("usuario")
    contrasena = request.args.get("password")
    resultado = inicioSesion.validarExistencia(usuario, contrasena)
    return resultado


@login_bp.route("/api/registrarUsuario", methods=["GET"])
def registrarUsuario():
    usuario = request.args.get("usuario")
    contrasena = request.args.get("password")
    resultado = registro.agregarUsuario(usuario, contrasena)
    return resultado
