import reflex as rx
from .form import formRegister
from .state import UserRegistered, FormState

def user_box(user_register: UserRegistered):
    return rx.vstack(
        rx.text(user_register.name),
        rx.text(user_register.email),
        rx.text(user_register.phone),
        rx.text(user_register.service),
        rx.text(user_register.description)
    )


def pageRegister() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="user-round", size=32),
                    # color_scheme="blue",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.heading(
                        "Registro en Obranet",
                        size="4",
                        weight="bold",
                    ),
                    rx.text(
                        "Completa el formulario para ofrecer tu trabajo",
                        size="2",
                    ),
                    # rx.cond(FormRegisterState.did_submit,FormRegisterState.thank_you,""),
                    spacing="1",
                    height="100%",
                ),
                height="100%",
                spacing="4",
                align_items="center",
                width="100%",
            ),
           
            rx.box(
                rx.foreach(FormState.users, user_box),
                width="100%"
            ),
            formRegister(),
            rx.divider(),
            rx.heading("Results"),
            # rx.text(FormRegisterState.form_data.to_string()),
            width="100%",
            direction="column",
            spacing="4",
        ),
        size="3",
    )
