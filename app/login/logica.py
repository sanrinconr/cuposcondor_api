from .modelos import UsuarioDAO
from app import jwt
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    set_access_cookies,
    set_refresh_cookies,
    jwt_refresh_token_required,
    get_jwt_identity,
    get_jwt_claims,
)
from flask import jsonify
import datetime


class Usuario:
    @staticmethod
    def registrarse(alias=None, contrasena=None):
        if alias:
            if contrasena:
                usuario = UsuarioDAO(alias, contrasena)
                res = usuario.guardar()
                if res == True:
                    salida = {
                        "alias": alias,
                        "registrado": True,
                    }
                    return salida
                elif isinstance(res, list):
                    return {
                        "alias": alias,
                        "registrado": False,
                        # "Error": res[0] if str(res[0]) == "1062" else "0000",
                        "Error": res[0],
                        # "Descripcion": res[1] if str(res[0]) == "1062" else "Desconocido",
                        "Descripcion": res[1],
                    }
                else:
                    return {
                        "alias": alias,
                        "registrado": False,
                        "Error": res[0],
                        "Descripcion": res[1],
                    }
            else:
                return {
                    "alias": alias,
                    "registrado": False,
                    "Error": "0000",
                    "Descripcion": "No se envio contrasena",
                }
        else:
            return {
                "registrado": False,
                "Error": "0000",
                "Descripcion": "No se envio alias",
            }

    @staticmethod
    def iniciar_sesion(json):
        if json:
            alias = json["alias"] if "alias" in json else None
            contrasena = json["contrasena"] if "contrasena" in json else None
        else:
            alias = None
            contrasena = None
        # if x: , valida que x no sea None
        if alias:
            if contrasena:
                usuario = UsuarioDAO.get_by_nombre(alias)
                if usuario:
                    valido = usuario.validar_contrasena(contrasena)
                    if valido:
                        access_token = create_access_token(json)
                        refresh_token = create_refresh_token(json)

                        salida = jsonify(
                            {
                                "alias": alias,
                                "logueado": True,
                                "token": access_token,
                                "refresh_token": refresh_token,
                            }
                        )
                        set_access_cookies(salida, access_token)
                        set_refresh_cookies(salida, refresh_token)
                        return salida
                    else:
                        return {
                            "alias": alias,
                            "logueado": False,
                            "Error": "0000",
                            "Descripcion": "Contrasena incorrecta",
                        }
                else:
                    return {
                        "alias": alias,
                        "logueado": False,
                        "Error": "0000",
                        "Descripcion": "El usuario no existe",
                    }
            else:
                return {
                    "alias": alias,
                    "logueado": False,
                    "Error": "0000",
                    "Descripcion": "No se envio contrasena",
                }
        else:
            return {
                "logueado": False,
                "Error": "0000",
                "Descripcion": "No se envio alias",
            }

    @jwt_refresh_token_required
    def refresh_token(json):
        access_token = create_access_token(json)
        resp = jsonify({"nuevo_token_generado": True, "token": access_token})
        set_access_cookies(resp, access_token)
        return resp

    # Se define que sera la identidad
    @jwt.user_identity_loader
    def user_identity_lookup(json):
        print("wefwe: " + str(get_jwt_identity()))
        if get_jwt_identity():
            print("weweoifjweoifjfwe: " + str(get_jwt_identity()))
            return get_jwt_identity()
        else:
            print("wefwe:weoifjweoif")
            return json["alias"]

    # Se agrega informacion al token, se llama cuando se utiliza create_access_token
    @jwt.user_claims_loader
    def add_claims_to_access_token(json):
        if json:
            ip = json["ip"] if "ip" in json else None
            userAgent = json["user-agent"] if "user-agent" in json else None
        else:
            ip = None
            userAgent = None
        return {"ip": ip, "user-agent": userAgent}
