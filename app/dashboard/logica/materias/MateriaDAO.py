from Materia import Materia


class MateriaDAO:
    correo = None
    nombre = None
    grupo = None
    url = None

    def __init__(materia):
        self.nombre = materia.nombre
        self.grupo = materia.grupo
        self.url = materia.url
        self.correo = materia.correo

    def guardar():
        self.guardarMateria(self.nombre, self.url, self.grupo, self.correo)

    def guardarMateria(nombre, url, grupo, correo):
        try:
            conexion = engine.connect()
            metadata = db.MetaData()
            tablaMateria = db.Table(
                "Materia", metadata, autoload=True, autoload_with=engine
            )
            query = db.insert(tablaMateria).values(
                nombreMateria=nombre, urlMateria=url, correo=correo,
            )
            res = conexion.execute(query)
            conexion.close()
            dict = {
                "nombre": usuarioPOST,
                "registrado": "si",
            }
            return jsonify(dict)
        except exc.OperationalError as e:
            # SI LA DB NO ESTA CONECTADA
            if str(e.orig.args[0]) == "2003":
                return "2003"
            return "ERROR DESCONOCIDO"
            return str(e.orig.args)
            # En caso de que se quiera ver de que trata el error
        except exc.DatabaseError as e:
            # ALIAS YA EXISTENTE
            if str(e.orig.args[0]) == "1062":
                dict = {
                    "usuario": usuarioPOST,
                    "registrado": "no",
                    "error": "ya registrado",
                    "codigo": "1062",
                }
                return jsonify(dict)
            return "ERROR DESCONOCIDO"
            return str(e.orig.args)
        except:
            return "ERROR DESCONOCIDO"
