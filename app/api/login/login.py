# Dependencias
from flask import request
from flask_login import current_user, login_user, logout_user
from app import login_manager

from app.api import api_bp

from app.api.modelos import Usuario
from app.api.modelos import db


@api_bp.route("/api/login/validarUsuario", methods=["GET"])
def APIvalidarUsuario(usu=None, contra=None):
    usuarioGet = request.args.get("usuario")
    contrasenaGet = request.args.get("contrasena")
    if current_user.is_authenticated:
        return "<html>YA AUTENTICADO</html>"
    usuario = Usuario.get_by_nombre(usuarioGet)
    if usuario.check_password(contrasenaGet) and usuario is not None:
        login_user(usuario, remember=True)
        return "Logueado!"

    return "Contrasena: " + str(usuario.contrasena)


@api_bp.route("/api/login/registrarUsuario", methods=["GET"])
def APIregistrarUsuario():
    usuario = request.args.get("usuario")
    contrasena = request.args.get("contrasena")
    u = Usuario(usuario, contrasena)
    u.guardar()
    return {"usuario": usuario, "valido": True}


@api_bp.route("/api/login/logout")
def logout():
    usuario = current_user.get_id()
    if usuario is not None:
        logout_user()
        return {"usuario": str(usuario), "deslogueado": True}
    else:
        return {"usuario": "Anonimo", "deslogueado": False}


@login_manager.user_loader
def load_user(nombre):
    return Usuario.get_by_nombre(nombre)
