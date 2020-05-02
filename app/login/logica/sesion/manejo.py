from flask import session


class sesion:
    @staticmethod
    def crear(usuario):
        session["usuario"] = usuario
        session["autenticado"] = 1

    def expirar():
        session.clear()
