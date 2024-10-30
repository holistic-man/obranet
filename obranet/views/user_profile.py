import reflex as rx
import obranet.styles.styles as styles
from obranet.routes import Route
from obranet.backend.states import UserListState
from obranet.models import Registrado
from obranet.components.user_info import user_info


def user_detail_content(user: Registrado):
    return rx.box(
        rx.flex(
            rx.box(
                rx.cond(
                    user.photo,
                    rx.image(
                        src=user.photo,
                        alt=f"Foto de perfil de {user.name} en Obranet",
                        height="12rem",
                        margin_left="auto",
                        margin_right="auto",
                        object_fit="cover",
                        border_radius="9999px",
                        width="12rem",
                    ),
                    rx.image(
                        src="/user_generico.jpeg",
                        alt=f"Foto de perfil generico en Obranet",
                        height="12rem",
                        margin_left="auto",
                        margin_right="auto",
                        object_fit="cover",
                        border_radius="9999px",
                        width="12rem",
                    ),
                ),
                margin_bottom=rx.breakpoints(
                    {"0px": "1.5rem", "768px": "0"}
                ),
                # width=rx.breakpoints({"768px": "33.333333%"}),
            ),
            rx.box(
                rx.heading(
                    user.name,
                    font_weight="700",
                    margin_bottom="0.5rem",
                    font_size="1.875rem",
                    line_height="2.25rem",
                    as_="h1",
                ),
                rx.text(
                    user.service,  
                    margin_bottom="1rem",
                    font_size="1.25rem",
                    line_height="1.75rem",
                ),
                rx.box(
                    rx.text(
                        rx.icon(
                            tag='mail',
                            # height="1rem",
                            display="inline-block",
                            margin_right="0.5rem",
                            # width="1rem",
                        ),
                        user.email,
                        padding_y="0.25rem",
                        
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
                        padding_y="0.25rem",
                        
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
                    
                    # margin_bottom="1rem",
                ),
                # padding_y="1rem",
                padding_left=rx.breakpoints({"768px": "2rem"}),
                text_align=["center","start"],
                width=rx.breakpoints({"768px": "66.666667%"}),
            ),
            display="flex",
            padding_y="2rem",
            flex_direction=rx.breakpoints(
                {"0px": "column", "768px": "row"}
            ),
        ),
        rx.box(
            rx.heading(
                "Sobre mi",
                padding_bottom="1em"
            ),
            rx.text(
                user.description,
                line_height="1.625",
            ),
            padding_y="1rem",
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
            padding_y="2rem"
        ),
        
       
    )


def user_profile() -> rx.Component:
    return rx.cond(
        UserListState.is_loaded,
        user_detail_content(UserListState.user),
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

