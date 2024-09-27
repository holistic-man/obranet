import reflex as rx




def create_large_centered_icon(alt_text, icon_tag):
    """Create a large centered icon with specified alt text and tag."""
    return rx.icon(
        alt=alt_text,
        tag=icon_tag,
        height="4rem",
        margin_bottom="1rem",
        margin_left="auto",
        margin_right="auto",
        width="4rem",
    )


def create_text(content):
    """Create a text element with specified color and content."""
    return rx.text(content)


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

def create_feature_box(
    icon_alt, icon_tag, title, description
):
    """Create a feature box with an icon, title, and description."""
    return rx.box(
        create_large_centered_icon(
            alt_text=icon_alt, icon_tag=icon_tag
        ),
        create_styled_heading(
            heading_level="h3",
            font_size="1.25rem",
            margin_bottom="0.5rem",
            content=title,
        ),
        create_text(
            content=description
        ),
        text_align="center",
    )

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


def how_it_works():
    """Create the 'How SkillConnect Works' section with steps."""
    return rx.box(
        create_centered_heading(
            content="Cómo Funciona Obranet"
        ),
        rx.box(
            create_feature_box(
                icon_alt="Create Profile Icon",
                icon_tag="user-plus",
                title="Crea un Perfil",
                description="Muestra tus habilidades y experiencia a clientes potenciales",
            ),
            create_feature_box(
                icon_alt="Search Icon",
                icon_tag="search",
                title="Busca Servicios",
                description="Encuentra el profesional adecuado para tus necesidades específicas",
            ),
            create_feature_box(
                icon_alt="Connect Icon",
                icon_tag="message-square",
                title="Conecta y Contrata",
                description="Comuníquese directamente y contrate con confianza",
            ),
            gap="2rem",
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "768px": "repeat(3, minmax(0, 1fr))",
                }
            ),
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
        padding_x="1.5rem",
        padding_y="4rem",
    )