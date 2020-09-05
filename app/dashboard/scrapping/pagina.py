import requests


class Consulta:
    @staticmethod
    def getPagina(url):
        r = requests.get(url)
        return r


class Analisis:
    pass
