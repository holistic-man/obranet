import reflex as rx
import obranet.utils as utils
import obranet.styles.styles as styles
from obranet.routes import Route
from obranet.components.navbar import navbar
from obranet.components.footer import footer
from obranet.views.register import form_register #, register_form
from obranet.state.PageState import PageState

@rx.page(
    route=Route.REGISTER.value,   
    title=utils.register_title,
    # description=utils.register_description,
    # image=utils.preview,
    # meta=utils.register_meta
    on_load=PageState.list_tabla
)
def register() -> rx.Component:
    return rx.box(
        navbar(),
        rx.container(
            # register_form(),
            form_register(PageState.list_info),
        ),
        footer(),
    )