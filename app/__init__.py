from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Instancia de la base de datos a usar
db = SQLAlchemy()
login_manager = LoginManager()


def create_app(settings_module="config.local"):
    "Creacion de la aplicacon dada una configuracion"

    app = Flask(__name__)

    ##SE CARGA LA CONFIGURACION CONFIGURACION
    app.config.from_object(settings_module)
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "mysql+pymysql://root:12345@localhost:3306/cuposcondor"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "APIvalidarUsuario"

    # BLUEPRINTS
    from .api import api_bp

    app.register_blueprint(api_bp)

    """
    from .login import login_bp

    app.register_blueprint(login_bp)

    #    from .dashboard import dashboard_bp

<<<<<<< Updated upstream
    #    app.register_blueprint(dashboard_bp)

    return app
=======
    app.register_blueprint(dashboard_bp)
    """

    # Generacion automatica de las tablas
    with app.app_context():
        # Se limpia toda la base de datos, usada por ahora para
        # trabajar la estructura, se debe quitar
        # db.drop_all()

        # Se crean las tablas pues se importo el blueprint de api
        # el cual a su vez importa el login y finalmente se importa
        # el modelo usuario c:
        db.create_all()
        return app
>>>>>>> Stashed changes
