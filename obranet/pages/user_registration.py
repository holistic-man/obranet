import reflex as rx
import obranet.utils as utils
import obranet.styles.styles as styles
from obranet.routes import Route
from obranet.components.navbar import navbar
from obranet.components.footer import footer
from obranet.views.user_register import user_register
# from obranet.state.RegisterState import RegisterState
from obranet.backend.states import RegisterState
from obranet.components.developed_by import developed_by


@rx.page(
    route=Route.USER_REGISTER.value,   
    title=utils.register_title,
    # description=utils.register_description,
    # image=utils.preview,
    # meta=utils.register_meta
    on_load=[RegisterState.reset_error_message,RegisterState.reset_success_message]
)
def user_registration() -> rx.Component:
    return rx.box(
        navbar(),
        rx.container(
            user_register(),
            # padding_y="2rem"
        ),
        rx.box(height="10vh"),
        footer(),
        developed_by()
    )