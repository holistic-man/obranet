from obranet.register.page import pageRegister
import reflex as rx

@rx.page(
    route="/demo"
)
def register() -> rx.Component:
    return pageRegister()
