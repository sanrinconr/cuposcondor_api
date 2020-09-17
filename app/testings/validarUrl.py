import requests


def validarUrl(url):
    desarrollo = False

    longitud = False
    dominio = False
    curl = False

    url = url.replace("view-source:", "")

    if len(url) > 530 or desarrollo == True:
        longitud = True
    if (
        url.find(
            "https://estudiantes.portaloas.udistrital.edu.co/academicopro/index.php"
        )
        != -1
        or desarrollo == True
    ):
        dominio = True

    try:
        html = requests.get(url).text
    except:
        html = None
    if html:
        if html.find('<table class="tabla_general">'):
            curl = True

    if longitud and dominio and curl:
        return True
    else:
        return False


if __name__ == "__main__":
    print(
        validarUrl(
            "https://estudiantes.portaloas.udistrital.edu.co/academicopro/index.php?index=JkWYBAdHPwdoaplK9N1C5GPekmL5arCq6J5jd2l6otNCj8mm5SOLJov2GWy9EazgVpWOf3K4AfOH--RgItDnKsc1SBbgeBUMFXENq8PLKFVgnx5psI7Sio5pAyE7roPxNv6YrOjlKgzehTztD-zBRm9aL2_0u3d07kWKKRRR25jpuX9Nbulvk9cHdAtaxAnjnwpJq1M9P64v1aHI3vzFUJaiXvpNwuxexmj5gvDFB9WCGpXSZexOSvZ99R4qKe-HOaH4MzqH8uBYXpzEImQTYQeeaIpzZyb62gTvLR37L2ksC38amMwPDEiRpVCT7CoT4pTT4JPZgVrdSpHaNm8-ADwVClPPbS8JDO5t6OBkeWcE_t2PjtqJIqy4AQh4yxaLRXrXIBe4U7gDf8bL2OTSyZfMYhL2fJ9vElWEeKB9ekMfkUwPuxkt7wf4X2ISNFuinbM0qZhFw2DgSYEhxawqYw6YqmzdgRneVy8WvfBJVF4OtDuZ56UjiA8xVodWWa7ve0wPM2YGLU2DPTWSfJgl4cnTpcnSc6JeJAcxmKlF_Cw"
        )
    )
