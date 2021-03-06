from .modelos import UsuarioDAO
from app import jwt
from flask_jwt_extended import (
    jwt_required,
    create_access_token,
    create_refresh_token,
    set_access_cookies,
    set_refresh_cookies,
    jwt_refresh_token_required,
    get_jwt_identity,
    get_jwt_claims,
    unset_jwt_cookies,
)
from flask import jsonify
import datetime


class Usuario:
    @staticmethod
    def registrarse(json):
        if json:
            alias = json["alias"] if "alias" in json else None
            contrasena = json["contrasena"] if "contrasena" in json else None
        else:
            alias = None
            contrasena = None
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
                        # "error": res[0] if str(res[0]) == "1062" else "0000",
                        "error": res[0],
                        # "Descripcion": res[1] if str(res[0]) == "1062" else "Desconocido",
                        "Descripcion": res[1],
                    }
                else:
                    return {
                        "alias": alias,
                        "registrado": False,
                        "error": res[0],
                        "Descripcion": res[1],
                    }
            else:
                return {
                    "alias": alias,
                    "registrado": False,
                    "error": "0000",
                    "Descripcion": "No se envio contrasena",
                }
        else:
            return {
                "registrado": False,
                "error": "0000",
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
                    # Si todo va bien se retorna true, de lo contrario se retorna la tupla que contiene numero y error
                    if isinstance(usuario, tuple) == False:
                        print("wefwefewfwewfweowjefoiwe")
                        valido = usuario.validar_contrasena(contrasena)
                        if valido:
                            access_token = create_access_token(identity=alias)
                            refresh_token = create_refresh_token(identity=alias)

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
                                "error": "0000",
                                "Descripcion": "Contrasena incorrecta",
                            }
                    else:
                        return {
                            "alias": alias,
                            "logueado": False,
                            "error": usuario[0],
                            "Descripcion": usuario[1],
                        }
                else:
                    return {
                        "alias": alias,
                        "logueado": False,
                        "error": "0000",
                        "Descripcion": "El usuario no existe",
                    }
            else:
                return {
                    "alias": alias,
                    "logueado": False,
                    "error": "0000",
                    "Descripcion": "No se envio contrasena",
                }
        else:
            return {
                "logueado": False,
                "error": "0000",
                "Descripcion": "No se envio alias",
            }

    @jwt_required
    def cerrar_sesion():
        try:
            response = jsonify(
                {
                    "sesionCerrada": True,
                }
            )
            unset_jwt_cookies(response)
            return response
        except:
            return {
                "sesionCerrada": False,
                "error": "desconocido",
            }

    @jwt_refresh_token_required
    def refresh_token():
        access_token = create_access_token(identity=get_jwt_identity())
        resp = jsonify(
            {"logueado": True, "nuevo_token_generado": True, "token": access_token}
        )
        set_access_cookies(resp, access_token)
        return resp
