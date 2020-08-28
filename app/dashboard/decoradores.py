from .logica.sesion.manejo import autenticado


def loginRequerido(funcion_a_decorar):
    def wrapper():
        print(autenticado())
        if autenticado() == True:
            return funcion_a_decorar()
        else:
            return "NO LOG"

    return wrapper
