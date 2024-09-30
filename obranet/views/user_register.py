import reflex as rx
import asyncio
from obranet.components.forms import register_form

def user_register():
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
                    spacing="1",
                    height="100%",
                ),
                height="100%",
                spacing="4",
                align_items="center",
                width="100%",
            ),
            
            register_form(),  

            height="100%",
            width="100%",
            direction="column",
            spacing="4",
        ),
        size="3",
        margin_y="4em"
    )
