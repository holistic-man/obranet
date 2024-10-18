import reflex as rx
from obranet.components.forms import contact_form



def create_icon(
    alt_text, icon_height, icon_tag, icon_width
):
    """Create an icon with specified alt text, tag, height, and width."""
    return rx.icon(
        alt=alt_text,
        tag=icon_tag,
        height=icon_height,
        width=icon_width,
    )



def create_h2_heading(margin_bottom, heading_text):
    """Create an h2 heading with predefined styles, specified margin bottom, and text."""
    return rx.heading(
        heading_text,
        font_weight="600",
        margin_bottom=margin_bottom,
        font_size="1.875rem",
        line_height="2.25rem",
        as_="h2",
    )


def create_small_icon(alt_text, icon_tag):
    """Create a small icon with specified alt text and tag."""
    return rx.icon(
        alt=alt_text,
        tag=icon_tag,
        height="1.5rem",
        margin_right="0.75rem",
        width="1.5rem",
    )


def create_text_span(span_text):
    """Create a text span with predefined color and specified text."""
    return rx.text.span(span_text)


def create_icon_with_text(icon_alt, icon_tag, text_content):
    """Create a flex container with an icon and text."""
    return rx.flex(
        create_small_icon(
            alt_text=icon_alt, icon_tag=icon_tag
        ),
        create_text_span(span_text=text_content),
        display="flex",
        align_items="center",
    )


def create_contact_hero_content():
    """Create the hero content for the contact section."""
    return rx.box(
        rx.heading(
            "Contáctanos",
            font_weight="700",
            margin_bottom="1rem",
            font_size="3rem",
            line_height="1",
            text_align="center",
            as_="h1",
        ),
        rx.text(
            "Estamos aquí para ayudar. Ponte en contacto con Obranet.",
            text_align="center",
            font_size="1.25rem",
            line_height="1.75rem",
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
        padding_left="1.5rem",
        padding_right="1.5rem",
        position="relative",
        z_index="10",
    )


def create_contact_hero_section():
    """Create the complete contact hero section with background and content."""
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
        create_contact_hero_content(),
        rx.box(
            position="absolute",
            bottom="0",
            left="0",
            right="0",
        ),
        class_name="bg-gradient-to-r from-blue-600 to-blue-800",
        padding_top="6rem",
        padding_bottom="6rem",
        position="relative",
        color="#ffffff",
    )


def create_contact_info_section():
    """Create the contact information section with heading, text, and contact details."""
    return rx.box(
        create_h2_heading(
            margin_bottom="1.5rem",
            heading_text="Pongámonos en contacto",
        ),
        rx.text(
            """¿Tienes preguntas sobre nuestros servicios? 
            ¿Necesitas apoyo con tu cuenta? ¿O quizás estás 
            interesado en asociarte con nosotros? ¡Nos 
            encantaría saber de ti! Completa el formulario 
            y nuestro equipo se pondrá en contacto contigo 
            lo antes posible.""",
            margin_bottom="1.5rem",
        ),
        rx.box(
            create_icon_with_text(
                icon_alt="Email",
                icon_tag="mail",
                text_content="obranetgroup@gmail.com",
            ),
            create_icon_with_text(
                icon_alt="Phone",
                icon_tag="phone",
                text_content="+56 9 6646 8556",
            ),
            create_icon_with_text(
                icon_alt="LinkedIn",
                icon_tag="linkedin",
                text_content="Obranet Group",
            ),
            display="flex",
            flex_direction="column",
            gap="1rem",
        ),
        margin_bottom=rx.breakpoints(
            {"0px": "2rem", "768px": "0"}
        ),
        width=rx.breakpoints({"768px": "50%"}),
    )

def create_contact_section():
    """Create the main contact section with info and form."""
    return rx.box(
        rx.flex(
            create_contact_info_section(),
            rx.box(
                contact_form(),
                padding_left=rx.breakpoints(
                    {"768px": "3rem"}
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
    )




def create_main_content():
    """Create the main content of the page including hero, contact, social, and CTA sections."""
    return rx.box(
        create_contact_hero_section(),
        rx.box(
            create_contact_section(),
            padding_y="4rem",
        ),
    )




