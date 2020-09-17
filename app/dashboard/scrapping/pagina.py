import requests


class Consulta:
    @staticmethod
    def getPagina(url):
        try:
            s = requests.get(url)
            print(s.status_code)
            if s.status_code == 200:
                return s.text
            else:
                return None
        except:
            return None
