class Materia:
    correo = None
    nombre = None
    grupo = None
    url = None

    def __init__(self, nombre, grupo, url, correo):
        self.nombre = nombre
        self.grupo = grupo
        self.url = url

    def guardar():
        dao = MateriaDAO(self)
        dao.guardar()
