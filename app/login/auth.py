from flask_restful import Resource


from flask import request, jsonify

from .logica import Usuario


class RegistrarApi(Resource):
    def post(self):
        try:
            body = request.get_json(force=True)
            return Usuario.registrarse(body)
        except:
            return jsonify(
                {
                    "registrado": False,
                    "Error": "0000",
                    "Descripcion": "desconocido",
                }
            )


class LoginApi(Resource):
    def post(self):
        try:
            print(str(request.get_json(force=True)))
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
        except:
            return {
                "logueado": False,
                "error": "desconocido",
            }
