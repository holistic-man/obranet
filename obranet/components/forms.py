import reflex as rx
from obranet.state.RegisterState import RegisterState
from obranet.backend.states import ContactState
# from obranet.components.forms import form_field
import obranet.constants as const


# def form_field(label: str, placeholder: str, type: str, name: str, error_message: str) -> rx.Component:
#     return rx.form.field(
#         rx.flex(
#             rx.form.label(label),
#             rx.form.control(
#                 rx.input(
#                     placeholder=placeholder, 
#                     type=type,
#                 ),
#                 as_child=True,
#             ),
#             rx.form.message(
#                 error_message,
#                 match="typeMismatch",
#             ),
#             direction="column",
#             spacing="1",
#         ),
#         name=name,
#         width="100%",
#     )


def form_field(label: str, placeholder: str, type: str, name: str) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.form.label(label),
            rx.form.control(
                rx.input(
                    placeholder=placeholder, 
                    type=type,
                ),
                as_child=True,
            ),
            rx.form.message(
                rx.hstack(
                    rx.text("Por favor, ingrese un valor válido", color="red"),
                ),
                match="typeMismatch",
            ),
            direction="column",
            spacing="1",
        ),
        name=name,
        width="100%",
    )

def register_form() -> rx.Component:
    return rx.form.root(
        rx.flex(
            rx.flex(
                form_field(
                    "Nombre Completo",
                    "Nombre Completo",
                    "text",
                    "name",
                ),
                form_field(
                    "Correo",
                    "ejemplo@gmail.com",
                    "email",
                    "email",
                ),
                spacing="3",
                flex_direction=[
                    "column",
                    "column",
                    "row",
                ],
            ),
            rx.flex(
                form_field(
                    "Celular", 
                    "+56 9 1234 5678",
                    "tel", 
                    "phone"
                ),
                rx.flex(
                    rx.text(
                        "Ubicación",
                        font_size="15px",
                        weight="medium",
                    ),
                    rx.select(
                        const.COMUNAS,
                        placeholder="Selecciona la comuna",
                        name="location"
                    ),
                    # select_location(),
                    direction="column",
                    justify="center",
                    spacing="1",
                    width="100%",
                ),  
                rx.flex(
                    rx.text(
                        "A qué te dedicas",
                        font_size="15px",
                        weight="medium",
                    ),
                    rx.select(
                        const.SERVICES,
                        placeholder="Selecciona a qué te dedicas",
                        name="service"
                    ),
                    direction="column",
                    justify="center",
                    spacing="1",
                    width="100%",
                ),  
                spacing="4",
                flex_direction=[
                    "column",
                    "row",
                    "row",
                ],
            ),
            rx.flex(
                rx.text(
                    "Descripción",
                    style={
                        "font-size": "15px",
                        "font-weight": "500",
                        "line-height": "35px",
                    },
                ),
                rx.text_area(
                    placeholder="Describe brevemente en qué consiste tu servicio y/o experiencia",
                    name="description",
                    resize="vertical",
                ),
                direction="column",
                spacing="1",
            ),
            rx.form.submit(
                rx.button(
                    "Registrar",
                    loading=RegisterState.is_submmiting,
                    cursor="pointer",
                ),
                as_child=True,    
            ),
            rx.cond(
                RegisterState.error_registration_message != "",
                rx.callout(
                    RegisterState.error_registration_message,
                    icon="triangle_alert",
                    color_scheme="red",
                    role="alert",
                )
            ),
            rx.cond(
                RegisterState.success_registration_message != "",
                rx.callout(
                    RegisterState.success_registration_message,
                    icon="circle-check-big",
                    color_scheme="green",
                    role="alert",
                )                
            ),
            direction="column",
            spacing="2",
            width="100%",
        ),
        on_submit=RegisterState.handle_submit,
        reset_on_submit=False,
    )
            

def contact_form() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="mail-plus", size=32),
                    color_scheme="blue",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.heading(
                        "Envíanos un mensaje",
                        size="4",
                        weight="bold",
                    ),
                    rx.text(
                        "Completa el formulario para contactarte con nosotros",
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
            rx.form.root(
                rx.flex(
                    rx.flex(
                        form_field(
                            "Nombre Completo",
                            "Nombre Completo",
                            "text",
                            "name",
                        ),
                        spacing="1",
                        direction="column",
                    ),
                    rx.flex(
                        form_field(
                            "Correo",
                            "ejemplo@gmail.com",
                            "email",
                            "email",
                        ),
                        spacing="1",
                        direction="column",
                    ),
                    rx.flex(
                        rx.text(
                            "Mensaje",
                            style={
                                "font-size": "15px",
                                "font-weight": "500",
                                "line-height": "35px",
                            },
                        ),
                        rx.text_area(
                            placeholder="Escribe aquí tu mensaje",
                            name="message",
                            resize="vertical",
                        ),
                        direction="column",
                        spacing="1",
                    ),
                    rx.form.submit(
                        rx.button(
                            "Enviar",
                            loading=ContactState.is_submmiting,
                            cursor="pointer",
                        ),
                        as_child=True,
                    ),
                    rx.cond(
                        ContactState.error_contact_message != "",
                        rx.callout(
                            ContactState.error_contact_message,
                            icon="triangle_alert",
                            color_scheme="red",
                            role="alert",
                        )
                    ),
                    rx.cond(
                        ContactState.success_contact_message != "",
                        rx.callout(
                            ContactState.success_contact_message,
                            icon="circle-check-big",
                            color_scheme="green",
                            role="alert",
                        )                
                    ),
                    
                    direction="column",
                    spacing="2",
                    width="100%",
                ),
                on_submit=ContactState.save_contact_form,
                reset_on_submit=True
            ),
            width="100%",
            direction="column",
            spacing="4",
        ),
        size="3",
    )


rx.form.root(
    rx.flex(
        rx.flex(
            rx.form.field(
                rx.flex(
                    form_field(
                        "Nombre Completo",
                        "Nombre Completo",
                        "text",
                        "name",
                    ),
                    spacing="1",
                    direction="column",
                ),
            ),
        ),
        rx.flex(
            rx.form.field(
                rx.flex(
                    form_field(
                        "Correo",
                        "ejemplo@gmail.com",
                        "email",
                        "email",
                    ),
                    rx.form.message(
                        "Por favor, ingrese un correo electrónico válido",
                        match="typeMismatch",
                    ),
                    spacing="1",
                    direction="column",
                ),
            ),
        ),
        # ... resto del código ...
    ),
    on_submit=ContactState.save_contact_form,
    reset_on_submit=True
)