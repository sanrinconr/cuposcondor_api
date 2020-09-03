"""

AUTOR: Juanjo

FECHA DE CREACIÓN: 24/05/2019

"""
import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from app import db

from flask_login import UserMixin
from sqlalchemy.exc import IntegrityError

# Distintos modelos usados de representacion para la base de datos
class UsuarioDAO(db.Model, UserMixin):
    __tablename__ = "usuario"
    # Modelo del usuario de la base de datos
    alias = db.Column(db.String(80), primary_key=True)
    contrasena = db.Column(db.String(128), nullable=False)
    fecha_registro = db.Column(
        db.DateTime, default=datetime.datetime.now, nullable=False
    )
    administrador = db.Column(db.Boolean, default=False, nullable=False)
    # En caso de ser distintas zonas horarias mejor:
    """
    fecha_registro = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, nullable=False
    )
    """
    # Constructor
    def __init__(self, name, contrasena):
        self.alias = name
        self.set_contrasena(contrasena)

    # Para cuando se imprima el objeto con print
    def __repr__(self):
        return f"<User {self.alias} contrasena {self.contrasena}>"

    # Establecer una contrasena al cliente hasheandola
    def set_contrasena(self, contrasena):
        self.contrasena = generate_password_hash(contrasena)

    # Verificar si una contrasena es correcta o no
    def validar_contrasena(self, contrasena):
        return check_password_hash(self.contrasena, contrasena)

    # Guardar el usuario actual en la db
    def guardar(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except IntegrityError as e:
            db.session.rollback()
            return e.orig.args
        except Exception as e:
            db.session.rollback()
            return e.orig.args
        except Exception as e:
            return e.orig.args

    @staticmethod
    # Se obtiene la instancia usuario a partir del nombre
    def get_by_nombre(nombre):
        try:
            return UsuarioDAO.query.get(nombre)
        except Exception as e:
            return e.orig.args

    @staticmethod
    # Se valida si un nombre es admin
    def es_admin(alias):
        usuario = UsuarioDAO.get_by_nombre(alias)
        return usuario.administrador
