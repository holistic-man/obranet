import reflex as rx
import obranet.utils as utils
import obranet.styles.styles as styles
from obranet.routes import Route
from obranet.components.navbar import navbar
from obranet.components.footer import footer
from obranet.views.contact.all import create_main_content
from obranet.views.cta import cta
from obranet.backend.states import ContactState

@rx.page(
    route=Route.CONTACT.value,   
    title=utils.contact_title,
    # description=utils.contact_description,
    # image=utils.preview,
    # meta=utils.contact_meta,
    on_load=[ContactState.reset_error_message,ContactState.reset_success_message]
)
def contact() -> rx.Component:
    return rx.box(
        navbar(),
        create_main_content(),
        cta(),
        footer()
    )