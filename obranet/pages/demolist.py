# from obranet.register.page import list_user_page
# from obranet.register.state import FormState
import reflex as rx

@rx.page(
    route="/demo/list",
    # on_load=FormState.list_users
)
def register_list() -> rx.Component:
    return rx.box()#list_user_page()
