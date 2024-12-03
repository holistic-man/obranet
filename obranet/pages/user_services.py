import reflex as rx
import obranet.utils as utils
import obranet.styles.styles as styles
from obranet.routes import Route
from obranet.components.navbar import navbar
from obranet.components.footer import footer
from obranet.views.user_list import user_list
from obranet.backend.states import UserListState
from obranet.components.developed_by import developed_by

from .no_pago import no_pago

@rx.page(
    route=Route.USER_SERVICES_LIST.value,   
    title=utils.services_title,
    # description=utils.services_description,
    # image=utils.preview,
    # meta=utils.services_meta
    # on_load=UserListState.reset_pagination #QUIZAS SACAS EL RESET PAGINATION
)
def user_services() -> rx.Component:
    return rx.box(
        no_pago()
        # navbar(),
        # rx.container(
        #     user_list(),
        #     size="4"    
           
        # ),
        # footer(),
        # developed_by()
    )

