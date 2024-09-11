from enum import Enum
import reflex as rx

class EMSize(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    BIGGER = "4em"


class Size(Enum):
    ZERO = "0"
    SMALL = "2"
    MEDIUM="3"
    DEFAULT = "4"
    LARGE = "6"
    BIG = "7"
    BIGGER = "8"
    VERY_BIG = "9"

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap",
    # "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap",
    # "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
    # "/css/styles.css"
]

BASE_STYLE = {
    "font-family":"Poppins"
    # rx.el.link(rel="stylesheet", href=)
    # "background_color": Color.BACKGROUND.value,
    # "font_family": Font.DEFAULT.value,
    # "font_weight":FontWeight.LIGHT.value,

    # rx.text: {
    #     "color":TextColor.TEXT.value
    # },

    # rx.link: {
    #     # "padding":Size.DEFAULT.value,
    #     "color":"orange",
    #     "text_decoration": "none",
    #     "_hover": {
    #         "text_decoration": "none",
    #         "color":"black",
    #         "transition": "color 0.4s ease, transform 0.4s ease",
    #         "transform": "scale(1.1)"
    #     },
    #     "transition":"color 0.4s ease, transform 0.4s ease",
    # }
    
}

