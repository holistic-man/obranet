import reflex as rx
import obranet.styles.styles as styles
from obranet.pages.index import index


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    theme=rx.theme(
        # appearance="light", 
        # accent_color="cyan" ,
        # panelBackground="solid", 
        # radius="small"
    ),
    head_components=[
#         rx.script(
#             src=f"https://www.googletagmanager.com/gtag/js?id={const.G_TAG}"),
#         rx.script(
#             f"""
# window.dataLayer = window.dataLayer || [];
# function gtag(){{dataLayer.push(arguments);}}
# gtag('js', new Date());
# gtag('config', '{const.G_TAG}');
# """
#         ),
    ],
)