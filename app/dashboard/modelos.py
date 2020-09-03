"""

AUTOR: Juanjo

FECHA DE CREACIÓN: 24/05/2019

"""
# Utilidades, para el tiempo y para validacion de espacios en blanco
import datetime
import re

# Para el manejo de hash
from werkzeug.security import generate_password_hash, check_password_hash

# La base de datos
from app import db


from flask_login import UserMixin

# Errores de la db
from sqlalchemy.exc import IntegrityError

# Distintos modelos usados de representacion para la base de datos
class MateriaDAO(db.Model):
    __tablename__ = "materia"
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
    # Constructor de una materia
    def __init__(self, nombre, url, alias):
        self.nombre = nombre
        self.url = url
        self.alias = alias

    # Guardar la materia actual en la db
    def guardar(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            return e.orig.args

    @staticmethod
    def get_materia_por_id(id, alias):
        return MateriaDAO.query.filter_by(alias=alias, id_materia=id).first()

    @staticmethod
    def get_materias_usuario(alias):
        return MateriaDAO.query.filter_by(alias=alias).all()
