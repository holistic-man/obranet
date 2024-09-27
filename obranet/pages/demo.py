# from obranet.register.page import pageRegister
# from obranet.register.state import FormState
import reflex as rx

@rx.page(
    route="/demo",
    # on_load=[FormState.reset_error_message,FormState.reset_success_message]
)
def register() -> rx.Component:
    return rx.box()#pageRegister()
