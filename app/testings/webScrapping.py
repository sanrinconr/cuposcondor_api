from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":
    grupo = "025-65"
    html = requests.get("http://localhost:6060/no/2")
    soup = BeautifulSoup(html.text, "lxml")
    filas = soup.find_all("tr", onmouseover="this.style.background='#F4F4EA'")
    for fila in filas:
        hijos = fila.findChildren("td")
        if hijos[0].get_text(strip=True) == grupo:
            boton = hijos[10].findChildren("button")
            if len(boton) == 0:
                print(
                    "No hay cupos "
                    + "("
                    + "Disponibles: "
                    + hijos[9].get_text(strip=True)
                    + " ,Cupos: "
                    + hijos[8].get_text(strip=True)
                    + ")"
                )
            else:
                print(
                    "Cupo!!"
                    + "("
                    + "Disponibles: "
                    + hijos[9].get_text(strip=True)
                    + " ,Cupos: "
                    + hijos[8].get_text(strip=True)
                    + ")"
                )

        # if td.get_text(strip=True) == grupo:
