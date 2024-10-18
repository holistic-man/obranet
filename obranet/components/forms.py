import reflex as rx
from obranet.backend.states import ContactState, RegisterState
import obranet.constants as const


def form_field(label: str, placeholder: str, type: str, name: str) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.form.label(label),
            rx.form.control(
                rx.input(
                    placeholder=placeholder, 
                    type=type,
                    required=True
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
                    "Celular", 
                    "+56 9 1234 5678", #ss
                    "tel", 
                    "phone"
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
            # rx.flex(
            #     rx.text(
            #         "Foto de Perfil",
            #         style={
            #             "font-size": "15px",
            #             "font-weight": "500",
            #             "line-height": "35px",
            #         },
            #     ),
            #     rx.upload(
            #         rx.vstack(
            #             rx.button(
            #                 "Seleccionar Archivo",
            #                 color_scheme="gray",
            #                 variant="surface",
            #                 type="button",
            #             ),
            #             # rx.text("Arrastra y suelta archivos acá o clickea Selecionar Archivo"),
            #         ),
            #         border=None,
            #         id="upload2",
            #         multiple=False,  # Solo permitir la subida de un archivo
            #         accept={"image/png": [".png"], "image/jpeg": [".jpg", ".jpeg"]},  # Limitar a imágenes PNG o JPEG
            #         on_drop=RegisterState.handle_upload(rx.upload_files(upload_id="upload2")),
            #         padding="0",
            #         name="photo",
                    
            #     ),
                
            #     direction="column",
            #     spacing="1",
            #     padding_bottom="1em"
            # ),
            # rx.upload(
            #     rx.vstack(
            #         rx.button(
            #             "Select File",
            #             # color=color,
            #             bg="white",
            #             # border=f"1px solid {color}",
            #         ),
            #         rx.text(
            #             "Drag and drop files here or click to select files"
            #         ),
            #     ),
            #     id="upload1",
            #     on_drop=RegisterState.handle_upload(
            #         rx.upload_files(upload_id="upload1")
            #     ),
            #     # border=f"1px dotted {color}",
            #     padding="5em",
            # ),
            rx.form.submit(
                rx.button(
                    "Registrar",
                    loading=RegisterState.is_loading,
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

