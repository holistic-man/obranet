import reflex as rx
from obranet.state.RegisterState import RegisterState
from obranet.routes import Route
from obranet.components.navbar import navbar
from obranet.components.footer import footer
from obranet.views.user_profile import user_profile


@rx.page(
        route=Route.USER_DETAIL.value, 
        on_load=RegisterState.get_user_detail
)
def user_detail():
    return rx.box(
        navbar(),
        rx.container(
            user_profile()
        ),
        footer(),
    )


