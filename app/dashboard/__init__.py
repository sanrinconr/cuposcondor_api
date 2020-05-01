from flask import Blueprint

dashboard_bp = Blueprint(
    "dashboard",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/static/dashboard",
)

from . import routes
