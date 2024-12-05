import reflex as rx
from obranet.backend.states import UserListState
from obranet.routes import Route
import obranet.utils as utils
from obranet.components.navbar import navbar
from obranet.components.footer import footer
from obranet.views.user_profile import user_profile
from obranet.components.developed_by import developed_by

from .no_pago import no_pago

@rx.page(
        route=Route.USER_DETAIL.value, 
        title=utils.user_detail_title,
        on_load=UserListState.get_user_detail
)
def user_detail():
    return rx.box(
        # no_pago()
        navbar(),
        rx.container(
            user_profile()
        ),
        footer(),
        developed_by()
    )


