import requests


class Consulta:
    @staticmethod
    def getPagina(url):
        s = requests.get(url).text
        return s
