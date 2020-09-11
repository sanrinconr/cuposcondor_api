from flask import Blueprint
from app import api
from .consultas import Misc

# El blueprint api
misc_bp = Blueprint("misc", __name__)

api.add_resource(Misc, "/api/misc/testConexion/")
