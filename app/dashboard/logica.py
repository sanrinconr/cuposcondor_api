from .modelos import MateriaDAO
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_restful import abort
from app import jwt

from flask import jsonify

# Web scrapping
from .scrapping.pagina import Consulta
from bs4 import BeautifulSoup


class Materia:
    @staticmethod
    @jwt_required
    # Agregar una materia a partir de un json que debe contener la clave nombre y url
    def agregar(json):
        # Se intentan obtener los datos del json
        nombre = json["nombre"] if "nombre" in json else None
        url = json["url"] if "url" in json else None
        grupo = json["grupo"] if "grupo" in json else None

        # Si nombre no es none
        if nombre:
            # Si url no es none
            if url:
                if grupo:
                    # Se obtiene la identidad actual
                    alias = get_jwt_identity()
                    # Resultado del ingreso en la db
                    res = MateriaDAO(nombre, url, grupo, alias).guardar()
                    if res == True:
                        return {"materia": nombre, "url": url, "registrada": True}
                    # En caso de que retorne algun error la db
                    else:
                        return {
                            "materia": nombre,
                            "url": url,
                            "registrada": False,
                            "Error": res[0],
                            "Descripcion": res[1],
                        }
                else:
                    return {
                        "materia": nombre,
                        "url": url,
                        "registrada": False,
                        "Error": "0000",
                        "Descripcion": "No se ingreso el grupo a buscar",
                    }

            else:
                return {
                    "materia": nombre,
                    "url": url,
                    "registrada": False,
                    "Error": "0000",
                    "Descripcion": "No se proporciono URL",
                }
        else:
            return {
                "materia": nombre,
                "url": url,
                "registrada": False,
                "Error": "0000",
                "Descripcion": "No se proporciono nombre",
            }

    @staticmethod
    @jwt_required
    def obtener(id_materia):
        materia = MateriaDAO.get_materia_por_id(id_materia, get_jwt_identity())
        if materia:
            salida = {
                "nombre": materia.nombre,
                "url": materia.url,
                "grupo": materia.grupo,
            }
            return salida
        else:
            abort(404, error_message="Materia no encontrada")

    @staticmethod
    @jwt_required
    def eliminar(id_materia):
        materia = MateriaDAO.get_materia_por_id(id_materia, get_jwt_identity())
        if materia:
            res = materia.eliminar()
            if res == True:
                return {"nombre": materia.nombre, "eliminada": True}
            elif isinstance(res, list):
                return {
                    "nombre": materia.nombre,
                    "eliminada": False,
                    "error": res[0],
                    "descripcion": res[1],
                }
            else:
                return {
                    "nombre": materia.nombre,
                    "eliminada": False,
                    "error": "0000",
                    "descripcion": "Desconocido",
                }
        else:
            abort(404, error_message="Materia no encontrada")


class Materias:
    @staticmethod
    @jwt_required
    def obtener():
        try:
            materias = MateriaDAO.get_materias_usuario(get_jwt_identity())
            salida = []
            for ele in materias:
                salida.append(
                    {
                        "id": ele.id_materia,
                        "nombre": ele.nombre,
                        "url": ele.url,
                        "grupo": ele.grupo,
                    }
                )
            return jsonify(salida)
        except Exception as e:
            return e.orig.args


class Cupo:
    @staticmethod
    def buscar(id_materia):
        try:
            materia = Materia.obtener(id_materia)
            if "url" in materia:
                html = Consulta.getPagina(materia["url"])
                soup = BeautifulSoup(html, "lxml")
                print(soup)
                grupo = materia["grupo"]
                filas = soup.find_all(
                    "tr", onmouseover="this.style.background='#F4F4EA'"
                )
                for fila in filas:
                    hijos = fila.findChildren("td")
                    if hijos[0].get_text(strip=True) == grupo:
                        boton = hijos[10].findChildren("button")
                        if len(boton) == 0:
                            return {
                                "materia": materia["nombre"],
                                "cupo": False,
                                "estado": "Sin cupo",
                                "disponibles": hijos[9].get_text(strip=True),
                                "cupos": hijos[8].get_text(strip=True),
                            }
                        else:
                            return {
                                "materia": materia["nombre"],
                                "cupo": False,
                                "estado": "Sin cupo",
                                "disponibles": hijos[9].get_text(strip=True),
                                "cupos": hijos[8].get_text(strip=True),
                            }

                # Si luego de recorrer todo el for no pudo retornar nada significa que el grupo nunca fue encontrado
                return {
                    "materia": materia["nombre"],
                    "cupo": "Error",
                    "error": "0000",
                    "estado": "No se pudo encontrar el grupo",
                }
            # En caso de que no se pueda obtener el json de materia (cosa que nunca deberia de pasar, de lo contrario estaria fallando la funcion llamada)
            return {
                "materia": materia["nombre"],
                "cupo": "Error",
                "error": "0000",
                "estado": "No se envio un url",
            }
        # En caso de no poder obtener la materia (normalmente db desconectada)
        except Exception as e:
            return {
                "cupo": "Error",
                "error": e.orig.args[0],
                "estado": e.orig.args[1],
            }
