import reflex as rx
import obranet.styles.styles as styles
from obranet.pages.index import index
from obranet.pages.user_registration import user_registration
from obranet.pages.user_services import user_services
from obranet.pages.user_detail import user_detail
from obranet.pages.demo import register
from obranet.pages.demolist import register_list
# from obranet.register.state import custom_backend_handler


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    # backend_exception_handler=custom_backend_handler,
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