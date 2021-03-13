from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_jwt_extended import JWTManager

from flask_cors import CORS

# Instancia de la base de datos a usar
db = SQLAlchemy()
# Instancia de la api
api = Api()

jwt = JWTManager()

cors = CORS()


def create_app(settings_module="config.local"):
    "Creacion de la aplicacon dada una configuracion"

    app = Flask(__name__)

    ##SE CARGA LA CONFIGURACION CONFIGURACION
    app.config.from_object(settings_module)
    print()
    # Primero usuario luego contrasena
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "mysql+pymysql://od8eeyaj22uz1bo8:tb7gr01nfcz2ra5p@un0jueuv2mam78uv.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/xaxwmccnpt1k36rv"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Se carga el contexto app en db y api

    from .login import login_bp

    app.register_blueprint(login_bp)

    from .dashboard import dashboard_bp

    app.register_blueprint(dashboard_bp)

    from .misc import misc_bp

    app.register_blueprint(misc_bp)

    db.init_app(app)
    api.init_app(app)
    jwt.init_app(app)
    cors.init_app(
        app,
        origins=["https://cuposcondor.site"],
        supports_credentials=True,
    )

    # Generacion automatica de las tablas
    with app.app_context():
        # Se limpia toda la base de datos, usada por ahora para
        # trabajar la estructura, se debe quitar
        #db.drop_all()

        # Se crean las tablas pues se importo el blueprint de api
        # el cual a su vez importa el login y finalmente se importa
        # el modelo usuario c:
        try:
            db.create_all()
        except:
            print("DB NO CONECTADA!!!!")
        return app
