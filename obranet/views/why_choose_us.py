import reflex as rx

def create_centered_heading(content):
    """Create a centered heading with default styles for section titles."""
    return rx.heading(
        content,
        font_weight="600",
        margin_bottom="3rem",
        font_size="1.875rem",
        line_height="2.25rem",
        text_align="center",
        as_="h2",
    )


def create_styled_heading(
    heading_level, font_size, margin_bottom, content
):
    """Create a styled heading with specified level, font size, margin, and content."""
    return rx.heading(
        content,
        font_weight="600",
        margin_bottom=margin_bottom,
        font_size=font_size,
        line_height="1.75rem",
        as_=heading_level,
    )


def create_text(content):
    """Create a text element with specified color and content."""
    return rx.text(content)


def create_info_box(title, description):
    """Create an information box with a title and description."""
    return rx.box(
        create_styled_heading(
            heading_level="h3",
            font_size="1.25rem",
            margin_bottom="0.5rem",
            content=title,
        ),
        create_text(
            content=description
        ),
    )

def create_colored_icon(alt_text, icon_color, icon_tag):
    """Create a colored icon with specified alt text, color, and tag."""
    return rx.icon(
        alt=alt_text,
        tag=icon_tag,
        height="3rem",
        margin_right="1rem",
        color=icon_color,
        width="3rem",
    )


def create_why_choose_us_content():
    return rx.box(
        rx.flex(
            create_colored_icon(
                alt_text="Verified Icon",
                icon_color="#10B981",
                icon_tag="clipboard-list",
            ),
            create_info_box(
                title="Variedad de Servicios",
                description="Ofrecemos una amplia variedad de servicios enfocados trabajos para el hogar.",
            ),
            display="flex",
            align_items="flex-start",
        ),
        rx.flex(
            create_colored_icon(
                alt_text="Quality Icon",
                icon_color="#F59E0B",
                icon_tag="star",
            ),
            create_info_box(
                title="Calidad Asegurada",
                description="Reseñas y calificaciones para garantizar un servicio de primera en todo momento.",
            ),
            display="flex",
            align_items="flex-start",
        ),
        rx.flex(
            create_colored_icon(
                alt_text="Security Icon",
                icon_color="#3B82F6",
                icon_tag="clock",
            ),
            create_info_box(
                title="Simpleza y Rapidez",
                description="Te ofrecemos acceso rápido y simple a los servicios que necesitas.",
            ),
            display="flex",
            align_items="flex-start",
        ),
        gap="2rem",
        display="grid",
        grid_template_columns=rx.breakpoints(
            {
                "0px": "repeat(1, minmax(0, 1fr))",
                "768px": "repeat(3, minmax(0, 1fr))",
            }
        ),
    )


def why_choose_us():
    return rx.box(
        rx.box(
            create_centered_heading(
                content="¿Por qué escoger Obranet?"
            ),
            create_why_choose_us_content(),
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
        ),
        id="about-us",
        # background_color="#ffffff",
        padding_top="4rem",
        padding_bottom="4rem",
    )
