from flask import Blueprint

# El blueprint login
login_bp = Blueprint(
    "login",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/static/login",
)

from . import api, login
