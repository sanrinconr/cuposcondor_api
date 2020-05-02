from flask import session


class sesion:
    @staticmethod
    def crearSesion(usuario):
        session["usuario"] = usuario
        session["autenticado"] = 1
