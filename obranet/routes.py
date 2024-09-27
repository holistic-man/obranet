from enum import Enum

class Route(Enum):
    INDEX = "/"
    USER_REGISTER = "/registro"
    USER_SERVICES_LIST = "/servicios"
    USER_DETAIL = "/servicios/[service]/[name]"
    SEARCH = "/busqueda"

    LOGO_OBRANET = "/obra2.png"
