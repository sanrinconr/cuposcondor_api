# Dependencias
import sqlalchemy as db
from sqlalchemy import exc
from flask import jsonify

# Engine
from app import engine


class inicioSesion:
    @staticmethod
    def validarExistencia(usuarioPOST, contrasenaPOST):
        try:
            conexion = engine.connect()
            metadata = db.MetaData()
            usuario = db.Table("Usuario", metadata, autoload=True, autoload_with=engine)
            query = db.select([usuario.columns.correo]).where(
                db.and_(
                    usuario.columns.correo == usuarioPOST,
                    usuario.columns.contrasena == contrasenaPOST,
                )
            )
            res = conexion.execute(query)
            resultSet = list(res.fetchall())
            conexion.close()
            if len(resultSet) == 1:
                dict = {
                    "usuario": usuarioPOST,
                    "valido": "si",
                }
                return jsonify(dict)
            else:
                dict = {
                    "usuario": usuarioPOST,
                    "valido": "no",
                }
                return jsonify(dict)
        except exc.OperationalError as e:
            if e.orig.args[0] == 2003:
                dict = {
                    "usuario": usuarioPOST,
                    "valido": "no",
                    "error": "base de datos no disponible",
                    "codigo": "2003",
                }
                return jsonify(dict)
            return str(e.orig.args[0])
            # En caso de que se quiera ver de que trata el error
            # print(e.orig.args[1])
        except exc.SQLAlchemyError as e:
            return str(e.orig.args)
            return "ERROR DESCONOCIDO"
