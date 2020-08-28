"""

AUTOR: Juanjo

FECHA DE CREACIÓN: 24/05/2019

"""
import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from app import db

from flask_login import UserMixin

# Distintos modelos usados de representacion para la base de datos
class Usuario(db.Model, UserMixin):
    # Modelo del usuario de la base de datos

    alias = db.Column(db.String(80), primary_key=True)
    contrasena = db.Column(db.String(128), nullable=False)
    fecha_registro = db.Column(
        db.DateTime, default=datetime.datetime.now, nullable=False
    )
    # En caso de ser distintas zonas horarias mejor:
    """
    fecha_registro = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, nullable=False
    )
    """

    def __init__(self, name, contrasena):
        self.alias = name
        self.set_contrasena(contrasena)

    def __repr__(self):
        return f"<User {self.alias} contrasena {self.contrasena}>"

    def set_contrasena(self, contrasena):
        self.contrasena = generate_password_hash(contrasena)

    def check_password(self, contrasena):
        return check_password_hash(self.contrasena, contrasena)

    def guardar(self):
        if self.alias is not None or self.contrasena is not None:
            db.session.add(self)
            db.session.commit()

    @staticmethod
    def get_by_nombre(nombre):
        return Usuario.query.get(nombre)

    def get_id(self):
        return self.alias


# Distintos modelos usados de representacion para la base de datos
class Materia(db.Model):
    # Modelo del usuario de la base de datos
    id_materia = db.Column(db.Integer, primary_key=True, autoincrement=True)
    alias = db.Column(db.String(80), db.ForeignKey("usuario.alias"))
    nombre = db.Column(db.String(80), nullable=False)
    url = db.Column(db.String(1000), nullable=False)
    fecha_creacion = db.Column(
        db.DateTime, default=datetime.datetime.now, nullable=False
    )
    # En caso de ser distintas zonas horarias mejor:
    """
    fecha_creacion = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, nullable=False
    )
    """

    def __init__(self, nombre, url, alias):
        self.nombre = nombre
        self.url = url
        self.alias = alias

    def guardar(self):
        if self.nombre is not None and self.url is not None and self.alias is not None:
            db.session.add(self)
            db.session.commit()
