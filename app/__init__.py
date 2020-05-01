from flask import Flask
import sqlalchemy as db

# Engine es una variable global para asi no generar mas de 1 engine causando problemas
engine = None


def create_app(settings_module="config.local"):
    app = Flask(__name__)

    ##SE CARGA LA CONFIGURACION CONFIGURACION
    app.config.from_object(settings_module)

    # Engine database
    global engine
    engine = db.create_engine(
        "mysql+pymysql://"
        + app.config["USUARIODB"]
        + ":"
        + app.config["CONTRASENADB"]
        + "@localhost:3306/cupos"
    )

    # BLUEPRINTS
    from .login import login_bp

    app.register_blueprint(login_bp)

    #    from .dashboard import dashboard_bp

    #    app.register_blueprint(dashboard_bp)

    return app
