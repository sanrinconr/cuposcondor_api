from flask import Blueprint

# El blueprint api
api_bp = Blueprint("api", __name__, template_folder="templates",)

# Este blueprint tendra dos ramas principales, el login y el dashboard
from .login import login
from .principal.dashboard import dashboard
