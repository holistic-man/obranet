import reflex as rx
from obranet.state.RegisterState import RegisterState
from obranet.components.forms.form_field import form_field

def formRegister() -> rx.Component:
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
                    rx.select.root(
                        rx.select.trigger(placeholder="Selecciona tu comuna"),
                        rx.select.content(
                            rx.select.item(
                                "Independencia", 
                                value="independencia"
                            ),
                             rx.select.item(
                                 "Santiago", 
                                value="santiago"
                            ),
                            rx.select.item(
                                "Recoleta", 
                                value="recoleta"
                            ),
                            rx.select.item(
                                "Conchalí", 
                                value="conchali"
                            ),
                            rx.select.item(
                                "Huechuraba", 
                                value="huechuraba"
                            ),
                        ),
                        name="location",        
                    ),  
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
                    rx.select.root(
                        rx.select.trigger(placeholder="Selecciona a qué te dedicas"),
                        rx.select.content(
                            rx.select.item(
                                "Pintor", 
                                value="pintor"
                            ),
                             rx.select.item(
                                 "Gasfiter", 
                                value="gasfiter"
                            ),
                            rx.select.item(
                                "Jardinero", 
                                value="jardinero"
                            ),
                            rx.select.item(
                                "Electricista", 
                                value="electricista"
                            ),
                            rx.select.item(
                                "Otro (Detalla en la descripción)", 
                                value="otro"
                            ),
                        ),
                        name="service",        
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
                    loading=RegisterState.is_submmiting
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
                    icon="triangle_alert",
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
    ),
            


