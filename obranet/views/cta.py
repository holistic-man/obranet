import reflex as rx
from obranet.routes import Route


def create_styled_button(
    hover_style, bg_color, href, content
):
    """Create a styled button with hover effects, background color, and link."""
    return rx.el.a(
        content,
        href=href,
        background_color=bg_color,
        transition_duration="300ms",
        font_weight="600",
        _hover=hover_style,
        padding_left="1.5rem",
        padding_right="1.5rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        margin_bottom = "1rem",
        border_radius="0.375rem",
        color="#ffffff",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )

def create_styled_paragraph(content):
    """Create a styled paragraph with default margin and font size."""
    return rx.text(
        content,
        margin_bottom="2rem",
        font_size="1.25rem",
        line_height="1.75rem",
    )


def cta():
    return rx.container(
        rx.box(
            rx.heading(
                "¿Listo para comenzar a utilizar Obranet?",
                font_weight="600",
                margin_bottom="2rem",
                font_size="1.875rem",
                line_height="2.25rem",
                as_="h2",
            ),
            create_styled_paragraph(
                content="Únete hoy a nuestra comunidad de profesionales capacitados y clientes satisfechos."
            ),
            rx.flex(
                # create_styled_button(
                #     hover_style={"background-color": "#1D4ED8"},
                #     bg_color="#2563EB",
                #     href=Route.REGISTER.value,
                #     content="Regístrate como profesional",
                # ),
                # create_styled_button(
                #     hover_style={"background-color": "#047857"},
                #     bg_color="#059669",
                #     href="#find-service",
                #     content="Encuentre proveedor de servicios",
                # ),
                rx.link(
                    rx.button(
                        "Registrate como profesional",
                        padding_x="1.5rem",
                        padding_y="0.75rem",
                        font_weight="600",
                        size="3",
                        width="100%",
                        cursor="pointer",
                        _hover={"background-color": "#1D4ED8"}
                    ),
                    href=Route.USER_REGISTER.value,
                    margin_bottom="1rem",
                ),
                rx.link(
                    rx.button(
                        "Encuentre proveedor de servicios",
                        padding_x="1.5rem",
                        padding_y="0.75rem",
                        font_weight="600",
                        size="3",
                        color_scheme="green",
                        width="100%",
                        cursor="pointer",
                        _hover={"background-color": "#047857"}
                    ),
                    href=Route.USER_SERVICES_LIST.value,
                ),
                display="flex",
                flex_direction=rx.breakpoints(
                    {"0px": "column", "768px": "row"}
                ),
                justify_content="center",
                column_gap="1rem",
            ),
            width="100%",
            style=rx.breakpoints(
                {
                    "640px": {"max-width": "640px"},
                    "768px": {"max-width": "768px"},
                    "1024px": {"max-width": "1024px"},
                    "1280px": {"max-width": "1280px"},
                    "1536px": {"max-width": "1536px"},
                }
            ),
            # margin_x="auto",
            # margin_right="auto",
            # padding_x="1.5rem",
            padding_y="4rem",
            text_align="center",
            
        ),
        bg="#0e2d70",
            color="white"
    )
