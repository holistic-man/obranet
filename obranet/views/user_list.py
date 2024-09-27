import reflex as rx
import obranet.styles.styles as styles
from obranet.routes import Route
from obranet.state.RegisterState import RegisterState
from obranet.models import Registrado
from obranet.components.user_info import user_info
from obranet.components.user_filter import user_filter

def scroll_to_top():
    return rx.call_script("window.scrollTo(0, 0)")

def user_list() -> rx.Component:
    return rx.box(
        rx.vstack(
            user_filter(),
            rx.cond(
                RegisterState.is_loaded,
                rx.box(
                    rx.foreach(RegisterState.users, user_info),
                    gap="2rem",
                    display="grid",
                    grid_template_columns=rx.breakpoints(
                        {
                            "0px": "repeat(1, minmax(0, 1fr))",
                            "768px": "repeat(2, minmax(0, 1fr))",
                            "1024px": "repeat(3, minmax(0, 1fr))",
                        }
                    ),
                ),

                rx.box(
                    rx.box(
                        rx.flex(
                            rx.skeleton(
                                rx.box(
                                    width=["430","200px"],
                                    height=["250px","200px"],
                                    padding="1em"
                                    # bg="grey"
                                )
                            ),
                            rx.vstack(
                                rx.skeleton(rx.heading("Texto Nombre")),
                                rx.skeleton(rx.text("TextoServicio")),
                                rx.skeleton(rx.text("Texto de ubicacion")),
                                padding="1em"
                            ),
                            # border="1px solid #ffffff",
                            max_width="56rem",
                            margin_left="auto",
                            margin_right="auto",
                            # padding="1.5rem",
                            border_radius="0.5rem",
                            
                            display="flex",
                            flex_direction=rx.breakpoints(
                                {"0px": "column", "768px": "row"}
                            ),
                            align_items=rx.breakpoints(
                                {"768px": "flex-start"}
                            ),
                        ),    
                        rx.vstack(
                            rx.skeleton(rx.heading("Texto Sobre MI"), display=["none","flex"]),
                            rx.skeleton(
                                rx.text(
                                    "TextoDescxtoDescripcionTextoDescxto",
                                    overflow="hidden",
                                    text_overflow="ellipsis",
                                ),
                                rx.text(
                                    "TextoDescxtoDescripcionTextoDescxto",
                                    overflow="hidden",
                                    text_overflow="ellipsis",
                                ),
                                rx.text(
                                    "TextoDescxtoDescripcionTextoDescxto",
                                    overflow="hidden",
                                    text_overflow="ellipsis",
                                    display=["none","flex"]
                                ),
                            ),    
                            rx.skeleton(rx.button("Ver Perfil", width="60%"), width="60%"),
                            padding="1em"
                        ),
                        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
                        border_radius="0.75rem",
                    ),
                    rx.box(
                        rx.flex(
                            rx.skeleton(
                                rx.box(
                                    width=["430","200px"],
                                    height=["250px","200px"],
                                    padding="1em"
                                    # bg="grey"
                                )
                            ),
                            rx.vstack(
                                rx.skeleton(rx.heading("Texto Nombre")),
                                rx.skeleton(rx.text("TextoServicio")),
                                rx.skeleton(rx.text("Texto de ubicacion")),
                                padding="1em"
                            ),
                            # border="1px solid #ffffff",
                            max_width="56rem",
                            margin_left="auto",
                            margin_right="auto",
                            # padding="1.5rem",
                            border_radius="0.5rem",
                            
                            display="flex",
                            flex_direction=rx.breakpoints(
                                {"0px": "column", "768px": "row"}
                            ),
                            align_items=rx.breakpoints(
                                {"768px": "flex-start"}
                            ),
                        ),    
                        rx.vstack(
                            rx.skeleton(rx.heading("Texto Sobre MI"), display=["none","flex"]),
                            rx.skeleton(
                                rx.text(
                                    "TextoDescxtoDescripcionTextoDescxto",
                                    overflow="hidden",
                                    text_overflow="ellipsis",
                                ),
                                rx.text(
                                    "TextoDescxtoDescripcionTextoDescxto",
                                    overflow="hidden",
                                    text_overflow="ellipsis",
                                ),
                                rx.text(
                                    "TextoDescxtoDescripcionTextoDescxto",
                                    overflow="hidden",
                                    text_overflow="ellipsis",
                                    display=["none","flex"]
                                ),
                            ),    
                            rx.skeleton(rx.button("Ver Perfil", width="60%"), width="60%"),
                            padding="1em"
                        ),
                        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
                        border_radius="0.75rem",
                    ),
                    rx.box(
                        rx.flex(
                            rx.skeleton(
                                rx.box(
                                    width=["430","200px"],
                                    height=["250px","200px"],
                                    padding="1em"
                                    # bg="grey"
                                )
                            ),
                            rx.vstack(
                                rx.skeleton(rx.heading("Texto Nombre")),
                                rx.skeleton(rx.text("TextoServicio")),
                                rx.skeleton(rx.text("Texto de ubicacion")),
                                padding="1em"
                            ),
                            # border="1px solid #ffffff",
                            max_width="56rem",
                            margin_left="auto",
                            margin_right="auto",
                            # padding="1.5rem",
                            border_radius="0.5rem",
                            
                            display="flex",
                            flex_direction=rx.breakpoints(
                                {"0px": "column", "768px": "row"}
                            ),
                            align_items=rx.breakpoints(
                                {"768px": "flex-start"}
                            ),
                        ),    
                        rx.vstack(
                            rx.skeleton(rx.heading("Texto Sobre MI"), display=["none","flex"]),
                            rx.skeleton(
                                rx.text(
                                    "TextoDescxtoDescripcionTextoDescxto",
                                    overflow="hidden",
                                    text_overflow="ellipsis",
                                ),
                                rx.text(
                                    "TextoDescxtoDescripcionTextoDescxto",
                                    overflow="hidden",
                                    text_overflow="ellipsis",
                                ),
                                rx.text(
                                    "TextoDescxtoDescripcionTextoDescxto",
                                    overflow="hidden",
                                    text_overflow="ellipsis",
                                    display=["none","flex"]
                                ),
                            ),    
                            rx.skeleton(rx.button("Ver Perfil", width="60%"), width="60%"),
                            padding="1em"
                        ),
                        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
                        border_radius="0.75rem",
                    ),
                    rx.box(
                        rx.flex(
                            rx.skeleton(
                                rx.box(
                                    width=["430","200px"],
                                    height=["250px","200px"],
                                    padding="1em"
                                    # bg="grey"
                                )
                            ),
                            rx.vstack(
                                rx.skeleton(rx.heading("Texto Nombre")),
                                rx.skeleton(rx.text("TextoServicio")),
                                rx.skeleton(rx.text("Texto de ubicacion")),
                                padding="1em"
                            ),
                            # border="1px solid #ffffff",
                            max_width="56rem",
                            margin_left="auto",
                            margin_right="auto",
                            # padding="1.5rem",
                            border_radius="0.5rem",
                            
                            display="flex",
                            flex_direction=rx.breakpoints(
                                {"0px": "column", "768px": "row"}
                            ),
                            align_items=rx.breakpoints(
                                {"768px": "flex-start"}
                            ),
                        ),    
                        rx.vstack(
                            rx.skeleton(rx.heading("Texto Sobre MI"), display=["none","flex"]),
                            rx.skeleton(
                                rx.text(
                                    "TextoDescxtoDescripcionTextoDescxto",
                                    overflow="hidden",
                                    text_overflow="ellipsis",
                                ),
                                rx.text(
                                    "TextoDescxtoDescripcionTextoDescxto",
                                    overflow="hidden",
                                    text_overflow="ellipsis",
                                ),
                                rx.text(
                                    "TextoDescxtoDescripcionTextoDescxto",
                                    overflow="hidden",
                                    text_overflow="ellipsis",
                                    display=["none","flex"]
                                ),
                            ),    
                            rx.skeleton(rx.button("Ver Perfil", width="60%"), width="60%"),
                            padding="1em"
                        ),
                        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
                        border_radius="0.75rem",
                    ),
                    rx.box(
                        rx.flex(
                            rx.skeleton(
                                rx.box(
                                    width=["430","200px"],
                                    height=["250px","200px"],
                                    padding="1em"
                                    # bg="grey"
                                )
                            ),
                            rx.vstack(
                                rx.skeleton(rx.heading("Texto Nombre")),
                                rx.skeleton(rx.text("TextoServicio")),
                                rx.skeleton(rx.text("Texto de ubicacion")),
                                padding="1em"
                            ),
                            # border="1px solid #ffffff",
                            max_width="56rem",
                            margin_left="auto",
                            margin_right="auto",
                            # padding="1.5rem",
                            border_radius="0.5rem",
                            
                            display="flex",
                            flex_direction=rx.breakpoints(
                                {"0px": "column", "768px": "row"}
                            ),
                            align_items=rx.breakpoints(
                                {"768px": "flex-start"}
                            ),
                        ),    
                        rx.vstack(
                            rx.skeleton(rx.heading("Texto Sobre MI"), display=["none","flex"]),
                            rx.skeleton(
                                rx.text(
                                    "TextoDescxtoDescripcionTextoDescxto",
                                    overflow="hidden",
                                    text_overflow="ellipsis",
                                ),
                                rx.text(
                                    "TextoDescxtoDescripcionTextoDescxto",
                                    overflow="hidden",
                                    text_overflow="ellipsis",
                                ),
                                rx.text(
                                    "TextoDescxtoDescripcionTextoDescxto",
                                    overflow="hidden",
                                    text_overflow="ellipsis",
                                    display=["none","flex"]
                                ),
                            ),    
                            rx.skeleton(rx.button("Ver Perfil", width="60%"), width="60%"),
                            padding="1em"
                        ),
                        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
                        border_radius="0.75rem",
                    ),
                    rx.box(
                        rx.flex(
                            rx.skeleton(
                                rx.box(
                                    width=["430","200px"],
                                    height=["250px","200px"],
                                    padding="1em"
                                    # bg="grey"
                                )
                            ),
                            rx.vstack(
                                rx.skeleton(rx.heading("Texto Nombre")),
                                rx.skeleton(rx.text("TextoServicio")),
                                rx.skeleton(rx.text("Texto de ubicacion")),
                                padding="1em"
                            ),
                            # border="1px solid #ffffff",
                            max_width="56rem",
                            margin_left="auto",
                            margin_right="auto",
                            # padding="1.5rem",
                            border_radius="0.5rem",
                            
                            display="flex",
                            flex_direction=rx.breakpoints(
                                {"0px": "column", "768px": "row"}
                            ),
                            align_items=rx.breakpoints(
                                {"768px": "flex-start"}
                            ),
                        ),    
                        rx.vstack(
                            rx.skeleton(rx.heading("Texto Sobre MI"), display=["none","flex"]),
                            rx.skeleton(
                                rx.text(
                                    "TextoDescxtoDescripcionTextoDescxto",
                                    overflow="hidden",
                                    text_overflow="ellipsis",
                                ),
                                rx.text(
                                    "TextoDescxtoDescripcionTextoDescxto",
                                    overflow="hidden",
                                    text_overflow="ellipsis",
                                ),
                                rx.text(
                                    "TextoDescxtoDescripcionTextoDescxto",
                                    overflow="hidden",
                                    text_overflow="ellipsis",
                                    display=["none","flex"]
                                ),
                            ),    
                            rx.skeleton(rx.button("Ver Perfil", width="60%"), width="60%"),
                            padding="1em"
                        ),
                        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
                        border_radius="0.75rem",
                    ),
                    
          
                    gap="2rem",
                    display="grid",
                    grid_template_columns=rx.breakpoints(
                        {
                            "0px": "repeat(1, minmax(0, 1fr))",
                            "768px": "repeat(2, minmax(0, 1fr))",
                            "1024px": "repeat(3, minmax(0, 1fr))",
                        }
                    ),
                ),
                
                
            ),
            rx.hstack(
                rx.button(
                    "Anterior",
                    on_click=[RegisterState.prev_page, scroll_to_top],
                    disabled=RegisterState.is_first_page,
                ),
                rx.text(f"Página {RegisterState.page_number} / {RegisterState.total_pages}"),
                rx.button(
                    "Siguiente",
                    on_click=[RegisterState.next_page, scroll_to_top],
                    disabled=RegisterState.is_last_page,
                ),
                align="center",
                justify="center",
                width="100%",
                padding_y="2em"
            ),
        ),
        on_mount=RegisterState.load_entries,
    )


#ESTA ES LA TABLA QUE SE VEN LOS DATOS EN FORMATO TABLA

def show_customer(user: Registrado):
    """Show a customer in a table row."""
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.phone),
        rx.table.cell(user.service),
    )



