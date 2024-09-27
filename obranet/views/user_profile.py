import reflex as rx
import obranet.styles.styles as styles
from obranet.routes import Route
from obranet.state.RegisterState import RegisterState
from obranet.models import Registrado
from obranet.components.user_info import user_info

def scroll_to_top():
    return rx.call_script("window.scrollTo(0, 0)")


def user_detail_content(user: Registrado):
    return rx.box(
        rx.box(
            rx.box(
                rx.image(
                    alt="Imagen de perfil de usuario registrado en Obranet",
                    src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/wlez7bzBYjVoQKsMR7g3GOBvjA1X9Ns9x9MJo0Zaef5Gz98mA/out-0.webp",
                    height=rx.breakpoints(
                        {"0px": "12rem", "768px": "100%"}
                    ),
                    object_fit="cover",
                    width=rx.breakpoints(
                        {"0px": "100%", "768px": "15rem"}
                    ),
                    border_radius="0.75rem"
                )       
            ),
            rx.box(
                rx.heading(
                    user.name,
                    font_weight="700",
                    line_height=rx.breakpoints(
                        {"0px": "2.25rem", "640px": "2.5rem"}
                    ),
                    margin_top="0.5rem",
                    font_size=rx.breakpoints(
                        {"0px": "1.875rem", "640px": "2.25rem"}
                    ),
                    # color="#111827",
                    letter_spacing="-0.025em",
                    as_="h2",
                ),
                rx.text(
                    rx.icon(
                        tag='contact',
                        # height="1rem",
                        display="inline-block",
                        margin_right="0.5rem",
                        # width="1rem",
                    ),
                    user.service,  
                    padding_top="1em",
                    padding_bottom="0.25rem"
                ),
                rx.text(
                    rx.icon(
                        tag='map-pin',
                        # height="1rem",
                        display="inline-block",
                        margin_right="0.5rem",
                        # width="1rem",
                    ),
                    user.location,
                    padding_y="0.25rem"
                ),
                rx.link(
                    rx.icon(
                        tag='phone',
                        # height="1rem",
                        display="inline-block",
                        margin_right="0.5rem",
                        # width="1rem",
                    ),
                    user.phone,
                    href=f"tel:{user.phone}",
                    padding_y="0.25rem"
                ),
                padding="1em",
            ),
            display=rx.breakpoints({"768px": "flex"}),
            # padding="1rem"
        ),
        rx.flex(
            rx.vstack(
                rx.heading("Sobre mi"),
                rx.text(
                    user.description,
                    overflow="hidden",
                    text_overflow="ellipsis",
                ),
                align_items="stretch",
                height="100%",
            ),
            direction="column",
            justify="space-between",
            height="200px",  # Ajusta esta altura según tus necesidades
            padding="1em",
        ),
        # COMENTARIOS Y CALIFICACIONES
        rx.box(
            rx.box(
                rx.flex(
                    rx.heading(
                        "Comentarios y calificaciones",
                        font_weight="600",
                        margin_bottom="1rem",
                        font_size="1.25rem",
                        line_height="1.75rem",
                        as_="h2",
                    ),
                    display="flex",
                    align_items="center",
                    margin_bottom="1rem",
                ),
                rx.box(
                    rx.flex(
                        rx.image(
                            src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/wlez7bzBYjVoQKsMR7g3GOBvjA1X9Ns9x9MJo0Zaef5Gz98mA/out-0.webp",
                            alt="alt_text",
                            height="2rem",
                            margin_right="0.5rem",
                            border_radius="9999px",
                            width="2rem",
                        ),
                        rx.text.span("Nombre Usuario", font_weight="600"),
                        rx.flex(
                            rx.icon(
                                tag="star",
                                height="1.25rem",
                                color="#FBBF24",
                                width="1.25rem",
                            ),
                            rx.icon(
                                tag="star",
                                height="1.25rem",
                                color="#FBBF24",
                                width="1.25rem",
                            ),
                            rx.icon(
                                tag="star",
                                height="1.25rem",
                                color="#FBBF24",
                                width="1.25rem",
                            ),
                            rx.icon(
                                tag="star",
                                height="1.25rem",
                                color="#FBBF24",
                                width="1.25rem",
                            ),
                            rx.icon(
                                tag="star",
                                height="1.25rem",
                                color="#FBBF24",
                                width="1.25rem",
                            ),
                            class_name="ml-auto",
                            display="flex",
                        ),
                        
                        # 
                        display="flex",
                        align_items="center",
                        margin_bottom="0.5rem",
                    ),
                    rx.text(
                        "Comentario de prueba solo para ver como se visualizaria un comentario en el perfil de un usuario en particular", 
                        max_width="75ch"
                    )
                ),
            ),
            rx.divider(),
            rx.box(
              
                rx.box(
                    rx.flex(
                        rx.image(
                            src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/wlez7bzBYjVoQKsMR7g3GOBvjA1X9Ns9x9MJo0Zaef5Gz98mA/out-0.webp",
                            alt="alt_text",
                            height="2rem",
                            margin_right="0.5rem",
                            border_radius="9999px",
                            width="2rem",
                        ),
                        rx.text.span("Nombre Usuario", font_weight="600"),
                        rx.flex(
                            rx.icon(
                                tag="star",
                                height="1.25rem",
                                color="#FBBF24",
                                width="1.25rem",
                            ),
                            rx.icon(
                                tag="star",
                                height="1.25rem",
                                color="#FBBF24",
                                width="1.25rem",
                            ),
                            rx.icon(
                                tag="star",
                                height="1.25rem",
                                color="#FBBF24",
                                width="1.25rem",
                            ),
                            rx.icon(
                                tag="star",
                                height="1.25rem",
                                color="#FBBF24",
                                width="1.25rem",
                            ),
                            rx.icon(
                                tag="star",
                                height="1.25rem",
                                color="#FBBF24",
                                width="1.25rem",
                            ),
                            class_name="ml-auto",
                            display="flex",
                        ),
                        
                        # 
                        display="flex",
                        align_items="center",
                        margin_bottom="0.5rem",
                    ),
                    rx.text(
                        "Comentario de prueba solo para ver como se visualizaria un comentario en el perfil de un usuario en particular", 
                        max_width="75ch"
                    )
                ),
            ),
            rx.divider(),
            rx.box(       
                rx.box(
                    rx.flex(
                        rx.image(
                            src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/wlez7bzBYjVoQKsMR7g3GOBvjA1X9Ns9x9MJo0Zaef5Gz98mA/out-0.webp",
                            alt="alt_text",
                            height="2rem",
                            margin_right="0.5rem",
                            border_radius="9999px",
                            width="2rem",
                        ),
                        rx.text.span("Nombre Usuario", font_weight="600"),
                        rx.flex(
                            rx.icon(
                                tag="star",
                                height="1.25rem",
                                color="#FBBF24",
                                width="1.25rem",
                            ),
                            rx.icon(
                                tag="star",
                                height="1.25rem",
                                color="#FBBF24",
                                width="1.25rem",
                            ),
                            rx.icon(
                                tag="star",
                                height="1.25rem",
                                color="#FBBF24",
                                width="1.25rem",
                            ),
                            rx.icon(
                                tag="star",
                                height="1.25rem",
                                color="#FBBF24",
                                width="1.25rem",
                            ),
                            rx.icon(
                                tag="star",
                                height="1.25rem",
                                color="#FBBF24",
                                width="1.25rem",
                            ),
                            class_name="ml-auto",
                            display="flex",
                        ),
                        
                        # 
                        display="flex",
                        align_items="center",
                        margin_bottom="0.5rem",
                    ),
                    rx.text(
                        "Comentario de prueba solo para ver como se visualizaria un comentario en el perfil de un usuario en particular", 
                        max_width="75ch"
                    )
                ),
            ),
            
            display="flex",
            flex_direction="column",
            gap="1rem",
        ),
        
        # background_color="black",
        overflow="hidden",
        border_radius="0.75rem",
        # box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
    )


def user_profile() -> rx.Component:
    return rx.cond(
        RegisterState.is_loaded,
        user_detail_content(RegisterState.user),
        rx.box(
            rx.flex(
                rx.skeleton(
                    rx.box(
                        width="300px",
                        height="250px",
                        padding="1em"
                    )
                ),
                rx.vstack(
                    rx.skeleton(rx.heading("Texto de Nombre")),
                    rx.skeleton(rx.text("Texto de servicio")),
                    rx.skeleton(rx.text("Texto de Numero")),
                    # rx.skeleton(rx.text("Texto de correo")),
                    # rx.skeleton(rx.text("Texto de ubicacion")),
                    padding="1em"
                ),
                max_width="56rem",
                margin_left="auto",
                margin_right="auto",
                padding="1.5rem",
                border_radius="0.5rem",
                # box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
                display="flex",
                flex_direction=rx.breakpoints(
                    {"0px": "column", "768px": "row"}
                ),
                align_items=rx.breakpoints(
                    {"768px": "flex-start"}
                ),
            ),
            rx.vstack(
                rx.vstack(
                    rx.skeleton(rx.heading("Texto de Nombre dsadafdsf fdsfsds")),
                    rx.skeleton(rx.heading("Texto de Nombre dsadafdsf fdsfsds Texto de Nombre dsadafdsf fdsfsds Texto de Nombre dsadafdsf fdsfsds")),
                    padding="1em"
                ),
                rx.vstack(
                    rx.skeleton(rx.heading("Texto de Nombre dsadafdsf fdsfsds")),
                    rx.skeleton(rx.heading("Texto de Nombre dsadafdsf fdsfsds Texto de Nombre dsadafdsf fdsfsds Texto de Nombre dsadafdsf fdsfsds")),
                    padding="1em"
                ),
                rx.vstack(
                    rx.skeleton(rx.heading("Texto de Nombre dsadafdsf fdsfsds")),
                    rx.skeleton(rx.heading("Texto de Nombre dsadafdsf fdsfsds Texto de Nombre dsadafdsf fdsfsds Texto de Nombre dsadafdsf fdsfsds")),
                    padding="1em"
                ),
                rx.vstack(
                    rx.skeleton(rx.heading("Texto de Nombre dsadafdsf fdsfsds")),
                    rx.skeleton(rx.heading("Texto de Nombre dsadafdsf fdsfsds Texto de Nombre dsadafdsf fdsfsds Texto de Nombre dsadafdsf fdsfsds")),
                    padding="1em"
                ),
               
            ),
        ),
    )

rx.cond(
        RegisterState.is_loaded,
        user_detail_content(RegisterState.user),
        rx.box(
            rx.flex(
                rx.skeleton(
                    rx.box(
                        width="300px",
                        height="250px",
                        padding="1em"
                    )
                ),
                rx.vstack(
                    rx.skeleton(rx.heading("Texto de Nombre")),
                    rx.skeleton(rx.text("Texto de servicio")),
                    rx.skeleton(rx.text("Texto de Numero")),
                    rx.skeleton(rx.text("Texto de correo")),
                    rx.skeleton(rx.text("Texto de ubicacion")),
                    padding="1em"
                ),
                max_width="56rem",
                margin_left="auto",
                margin_right="auto",
                padding="1.5rem",
                border_radius="0.5rem",
                box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
                display="flex",
                flex_direction=rx.breakpoints(
                    {"0px": "column", "768px": "row"}
                ),
                align_items=rx.breakpoints(
                    {"768px": "flex-start"}
                ),
            ),
        )
    )

rx.box(
        rx.vstack(
            rx.cond(
                RegisterState.is_loaded,
                user_detail_content(RegisterState.user),
                
                # SKELETON DE LOS BOX DE USUARIOS
                rx.box(
                    rx.flex(
                        rx.skeleton(
                            rx.box(
                                width="300px",
                                height="250px",
                                padding="1em"
                                # bg="grey"
                            )
                        ),
                        rx.vstack(
                            rx.skeleton(rx.heading("Texto de Nommbre")),
                            rx.skeleton(rx.text("Texto de servicio")),
                            rx.skeleton(rx.text("Texto de Numero")),
                            rx.skeleton(rx.text("Texto de correo")),
                            rx.skeleton(rx.text("Texto de ubicacion")),
                            padding="1em"
                        ),
                        # border="1px solid #ffffff",
                        max_width="56rem",
                        margin_left="auto",
                        margin_right="auto",
                        padding="1.5rem",
                        border_radius="0.5rem",
                        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
                        display="flex",
                        flex_direction=rx.breakpoints(
                            {"0px": "column", "768px": "row"}
                        ),
                        align_items=rx.breakpoints(
                            {"768px": "flex-start"}
                        ),
                    ),    
                )    
            ),
            
        ),
    )

