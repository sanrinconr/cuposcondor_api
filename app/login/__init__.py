from flask import Blueprint
from app import api
from .auth import RegistrarApi, LoginApi

# El blueprint api
login_bp = Blueprint("login", __name__)

api.add_resource(RegistrarApi, "/api/auth/registrar/")
api.add_resource(LoginApi, "/api/auth/login/")
