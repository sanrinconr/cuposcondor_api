# Dependencias
import sqlalchemy as db
from sqlalchemy import exc, event
from flask import jsonify
from datetime import datetime
from validate_email import validate_email
# Engine
from app import engine


class registro:
    @staticmethod
    def agregarUsuario(usuarioPOST, contrasenaPOST):
        if registro.validarDatos(usuarioPOST,contrasenaPOST) == False :
            dict = {
                "usuario": usuarioPOST,
                "registrado": "no",
                "error":"email no valido",
                "codigo":"desconocido",
            }
            return jsonify(dict)
        try:
            conexion = engine.connect()
            metadata = db.MetaData()
            tablaUsuario = db.Table(
                "Usuario", metadata, autoload=True, autoload_with=engine
            )
            query = db.insert(tablaUsuario).values(
                correo=usuarioPOST, contrasena=contrasenaPOST, fRegistro=datetime.now(),
            )
            res = conexion.execute(query)
            conexion.close()
            dict = {
                "usuario": usuarioPOST,
                "registrado": "si",
            }
            return jsonify(dict)
        except exc.OperationalError as e:
            # SI LA DB NO ESTA CONECTADA
            if str(e.orig.args[0]) == "2003":
                return "2003"
            return "ERROR DESCONOCIDO"
            return str(e.orig.args)
            # En caso de que se quiera ver de que trata el error
        except exc.DatabaseError as e:
            # ALIAS YA EXISTENTE
            if str(e.orig.args[0]) == "1062":
                dict = {
                    "usuario": usuarioPOST,
                    "registrado": "no",
                    "error": "ya registrado",
                    "codigo": "1062",
                }
                return jsonify(dict)
            return "ERROR DESCONOCIDO"
            return str(e.orig.args)
        except:
            return "ERROR DESCONOCIDO"

    @staticmethod
    def validarDatos(usuario,contrasena):
        is_valid = validate_email(usuario)
        return is_valid
