import reflex as rx
import obranet.utils as utils
import obranet.styles.styles as styles
from obranet.routes import Route
from obranet.components.navbar import navbar
from obranet.components.footer import footer
from obranet.views.user_list import user_list
from obranet.backend.states import UserListState
#lineadecambio


@rx.page(
    route=Route.USER_SERVICES_LIST.value,   
    title=utils.services_title,
    # description=utils.services_description,
    # image=utils.preview,
    # meta=utils.services_meta
    on_load=UserListState.reset_pagination #QUIZAS SACAS EL RESET PAGINATION
)
def user_services() -> rx.Component:
    return rx.box(
        navbar(),
        # rx.box(
        #     user_list(),
        #     max_width="1600px"
        # ),
        rx.container(
            user_list(),
            # max_width="1600px",
            # center_content=True,
            size="4"    
           
        ),
        
        footer(),
    )


# def user_info(user:Registrado) -> rx.Component:
#     return rx.box(
#         rx.text(user.name, user.email, user.service),
#         padding="1em"
#     )



# def list_user_page() -> rx.Component:
#     return rx.box(
#         rx.vstack(
#             rx.heading("Lista de usuario registrados en la BD de obranet"),
#             # rx.foreach(RegisterState.users,user_info)

#         )
#     )
