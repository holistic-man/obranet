import reflex as rx 
from obranet.routes import Route

def header_content() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.box(
               rx.heading(
                    "Ofrece y/o encuentra tus servicios con profesionales capacitados",
                    font_weight="700",
                    line_height="1",
                    margin_bottom="1.5rem",
                    font_size="3rem",
                    as_="h1",
                ),
                rx.text(
                    "Conecta con expertos de confianza para todas las mejoras que necesite para tu casa. Trabajo de calidad, satisfacción garantizada.",
                    margin_bottom="2rem",
                    font_size="1.25rem",
                    line_height="1.75rem",
                    # max_width="50ch"
                ),
                rx.flex(
                    rx.el.a(
                        "Contrata un servicio",
                        href=Route.USER_SERVICES_LIST.value,
                        background_color="#ffffff",
                        border_width="2px",
                        border_color="#ffffff",
                        transition_duration="300ms",
                        font_weight="600",
                        _hover={"background-color": "#F3F4F6"},
                        padding_left="2rem",
                        padding_right="2rem",
                        padding_top="0.75rem",
                        padding_bottom="0.75rem",
                        border_radius="9999px",
                        color="#2563EB",
                        text_align="center",
                        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
                        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
                    ),
                    rx.el.a(
                        "Ofrece tu servicio",
                        href=Route.USER_REGISTER.value,
                        background_color="transparent",
                        border_width="2px",
                        border_color="#ffffff",
                        transition_duration="300ms",
                        font_weight="600",
                        _hover={
                            "background-color": "#ffffff",
                            "color": "#2563EB",
                        },
                        padding_left="2rem",
                        padding_right="2rem",
                        padding_top="0.75rem",
                        padding_bottom="0.75rem",
                        border_radius="9999px",
                        text_align="center",
                        color="#ffffff",
                        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
                        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
                    ),
                    display="flex",
                    flex_direction=rx.breakpoints(
                        {"0px": "column", "640px": "row"}
                    ),
                    gap=rx.breakpoints(
                        {"0px": "1rem", "640px": "0"}
                    ),
                    column_gap=rx.breakpoints({"640px": "1rem"}),
                ),
                margin_bottom=rx.breakpoints(
                    {"0px": "2rem", "768px": "0"}
                ),
                width=rx.breakpoints({"768px": "50%"}), 
            ),
            rx.box(
                rx.image(
                    alt="Happy homeowner with skilled professional working on home improvement project",
                    src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/HkfM7iZdVZRVeUfDCkf88xNqNo4U1J0Ny4N6AoN9fkxLn4UbC/out-0.webp",
                    border_radius="0.5rem",
                    box_shadow="0 25px 50px -12px rgba(0, 0, 0, 0.25)",
                ),
                width=rx.breakpoints({"768px": "50%"}),
            ),
            display="flex",
            flex_direction=rx.breakpoints(
                {"0px": "column", "768px": "row"}
            ),
            align_items="center",
            justify_content="space-between",
        ),
        width="100%",
    )


def header() -> rx.Component:
    return rx.box(
        rx.box(
            position="absolute",
            background_color="#000000",
            top="0",
            right="0",
            bottom="0",
            left="0",
            opacity="0.5",
        ),
        rx.box(
            header_content(),
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
            margin_left="auto",
            margin_right="auto",
            padding_left="1.5rem",
            padding_right="1.5rem",
            position="relative",
            z_index="10",
        ),
        rx.box(
            position="absolute",
            bottom="0",
            left="0",
            right="0",
        ),
        class_name="bg-gradient-to-r from-blue-600 to-blue-800",
        padding_top="5rem",
        padding_bottom="5rem",
        position="relative",
        color="#ffffff",
    )