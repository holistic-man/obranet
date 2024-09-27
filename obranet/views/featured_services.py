import reflex as rx

def create_responsive_image(alt_text, image_src):
    """Create a responsive image component with full width and height coverage."""
    return rx.image(
        src=image_src,
        alt=alt_text,
        height="100%",
        object_fit="cover",
        width="100%",
    )


def create_image_container(image_alt, image_src):
    """Create a container for an image with fixed height and hidden overflow."""
    return rx.box(
        create_responsive_image(
            alt_text=image_alt, image_src=image_src
        ),
        height="12rem",
        overflow="hidden",
    )


def create_service_heading(heading_text):
    """Create a styled heading for a service category."""
    return rx.heading(
        heading_text,
        font_weight="600",
        padding_top="1rem",
        padding_bottom="1rem",
        text_align="center",
        color="#1F2937",
        font_size="1.25rem",
        line_height="1.75rem",
        as_="h3",
    )


def create_service_card(image_alt, image_src, service_name):
    """Create a service card with an image and heading, including hover effects."""
    return rx.box(
        create_image_container(
            image_alt=image_alt, image_src=image_src
        ),
        create_service_heading(heading_text=service_name),
        class_name="transform",
        background_color="#ffffff",
        transition_duration="300ms",
        _hover={"transform": "scale(1.05)"},
        overflow="hidden",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_view_all_services_button():
    """Create a styled button to view all services."""
    return rx.el.a(
        "Ver Todos los Servicios",
        href="#",
        # background_color="#2563EB",
        transition_duration="300ms",
        font_weight="600",
        _hover={
            "background-color": "#1D4ED8",
            "box-shadow": "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
        },
        display="inline-block",
        padding_left="2rem",
        padding_right="2rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="9999px",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
        # color="#ffffff",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_featured_services_section():
    """Create the featured services section with a heading, service cards, and a view all button."""
    return rx.box(
        rx.heading(
            "Servicios Destacados",
            font_weight="600",
            margin_bottom="3rem",
            font_size="1.875rem",
            line_height="2.25rem",
            text_align="center",
            # color="#1F2937",
            as_="h2",
        ),
        rx.box(
            create_service_card(
                image_alt="Pintor trabajando en una pared",
                image_src="/pintor.jpg",
                service_name="Pintor",
            ),
            create_service_card(
                image_alt="Gasfiter reparando una tubería",
                image_src="/gasfiter.jpg",
                service_name="Gasfiter",
            ),
            create_service_card(
                image_alt="Maestro constructor arreglando el segundo piso de una casa",
                image_src="/maestrogeneral.png",
                service_name="Maestro Constructor",
            ),
            create_service_card(
                image_alt="Fumigador exterminando plagas",
                image_src="/fumigador.jpg",
                service_name="Fumigador",
            ),
            gap="2rem",
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "640px": "repeat(2, minmax(0, 1fr))",
                    "1024px": "repeat(4, minmax(0, 1fr))",
                }
            ),
        ),
        rx.box(
            create_view_all_services_button(),
            margin_top="3rem",
            text_align="center",
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
        margin_left="auto",
        margin_right="auto",
        padding_left=rx.breakpoints(
            {
                "0px": "1rem",
                "640px": "1.5rem",
                "1024px": "2rem",
            }
        ),
        padding_right=rx.breakpoints(
            {
                "0px": "1rem",
                "640px": "1.5rem",
                "1024px": "2rem",
            }
        ),
    )


def feature_services():
    """Render the entire services page, including the featured services section."""
    return rx.fragment(
        rx.box(
            rx.box(
                create_featured_services_section(),
                # background_color="#F3F4F6",
                padding_top="4rem",
                padding_bottom="4rem",

            ),

        )
    )