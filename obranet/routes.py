from enum import Enum

class Route(Enum):
    INDEX = "/"
    USER_REGISTER = "/registro"
    USER_SERVICES_LIST = "/servicios"
    USER_DETAIL = "/servicios/[service]/[name]"
    ABOUT_US = "/nosotros"
    CONTACT = "/contacto"
    BLOG ="#"
    HOW_IT_WORKS = "#"
    Q_AND_A="#"

    LOGO_OBRANET = "/obra2.png"
