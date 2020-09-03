from flask_restful import Resource


from flask import request

from .logica import Usuario


class RegistrarApi(Resource):
    def post(self):
        body = request.get_json()
        return Usuario.registrarse(body["alias"], body["contrasena"])


class LoginApi(Resource):
    def post(self):
        body = request.get_json()
        body.update({"ip": request.remote_addr})

        # En caso de que refresh_token este definido en true se hace el refresco del token
        # En caso contraro se procede a iniciar sesion normal
        try:
            if body["refresh_token"] == "True":
                return Usuario.refresh_token()
            raise KeyError
        except KeyError:
            return Usuario.iniciar_sesion(body)
