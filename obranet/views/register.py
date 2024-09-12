import reflex as rx
import asyncio

from obranet.components.form_field import form_field

class FormRegisterState(rx.State):
    form_data: dict = {}
    did_submit: bool = False

    @rx.var
    def thank_you(self):
        name= self.form_data.get("name") or ""
        return f"Gracias {name}".strip() + "!"

    async def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        self.did_submit = True
        yield
        await asyncio.sleep(2)
        self.did_submit = False
        yield

def form_register():
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
                        "Completa el formulario para ofrecer tu servicio",
                        size="2",
                    ),
                    rx.cond(FormRegisterState.did_submit,FormRegisterState.thank_you,""),
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
                            "Celular",
                            "tel", 
                            "phone"
                        ),
                        rx.flex(
                            rx.text(
                                "Oficio",
                                font_size="15px",
                                weight="medium",
                            ),
                            rx.select.root(
                                rx.select.trigger(placeholder="Selecciona tu Oficio"),
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
                                        "Otro", 
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
                        
                        spacing="3",
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
                        rx.button("Registrar"),
                        as_child=True,
                    ),

                    rx.vstack(
                        rx.button("Submit", type="submit"),
                    ),
                    direction="column",
                    spacing="2",
                    width="100%",
                ),

                on_submit=FormRegisterState.handle_submit,
                reset_on_submit=True,
            ),
            rx.divider(),
            rx.heading("Results"),
            rx.text(FormRegisterState.form_data.to_string()),
            width="100%",
            direction="column",
            spacing="4",
        ),
        size="3",
    )


# def form_field(
#     label: str, placeholder: str, type: str, name: str
# ) -> rx.Component:
#     return rx.form.field(
#         rx.flex(
#             rx.form.label(label),
#             rx.form.control(
#                 rx.input(
#                     placeholder=placeholder, type=type
#                 ),
#                 as_child=True,
#             ),
#             direction="column",
#             spacing="1",
#         ),
#         name=name,
#         width="100%",
#     )


# def register_form() -> rx.Component:
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
                        "Registrate en Obranet",
                        size="4",
                        weight="bold",
                    ),
                    rx.text(
                        "Completa el formulario para ofrecer tu servicio",
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
                            "first_name",
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
                            "row",
                            "row",
                        ],
                    ),
                    rx.flex(
                        form_field(
                            "Celular", 
                            "Celular",
                            "tel", 
                            "phone"
                        ),
                        form_field(
                            "Last Name",
                            "Last Name",
                            "text",
                            "last_name",
                        ),
                        spacing="3",
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
                        rx.button("Registrar"),
                        as_child=True,
                    ),
                    direction="column",
                    spacing="2",
                    width="100%",
                ),
                on_submit=lambda form_data: rx.window_alert(
                    form_data.to_string()
                ),
                reset_on_submit=True,
            ),
            width="100%",
            direction="column",
            spacing="4",
        ),
        size="3",
    )