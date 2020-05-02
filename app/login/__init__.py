from flask import Blueprint

login_bp = Blueprint(
    "login",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/static/login",
)

from . import routes, api, login
