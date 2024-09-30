import reflex as rx 



def create_centered_heading(content):
    """Create a centered heading with predefined styles."""
    return rx.heading(
        content,
        font_weight="600",
        margin_bottom="3rem",
        font_size="1.875rem",
        line_height="2.25rem",
        text_align="center",
        as_="h2",
    )


def create_custom_heading(
    heading_type, font_size, line_height, content
):
    """Create a custom heading with specified type, font size, line height, and content."""
    return rx.heading(
        content,
        font_weight="600",
        margin_bottom="1rem",
        font_size=font_size,
        line_height=line_height,
        as_=heading_type,
    )



def create_blue_subheading(content):
    """Create a blue subheading with predefined styles."""
    return rx.heading(
        content,
        font_weight="600",
        margin_bottom="1rem",
        font_size="1.25rem",
        line_height="1.75rem",
        as_="h3",
    )


def create_info_box(title, description):
    """Create an info box with a title and description."""
    return rx.box(
        create_blue_subheading(content=title),
        rx.text(description),
        border_radius="0.5rem",
        padding="1.5em",
        box_shadow = rx.color_mode_cond(
            light="0 0 10px rgba(0, 0, 0, 0.2)",
            dark="0 0 10px rgba(255, 255, 255, 0.2)"
        ),
        # box_shadow="0 0 10px rgba(255, 255, 255, 0.1)"#"0 4px 8px rgba(0, 0, 0, 0.1), 0 2px 6px rgba(0, 0, 0, 0.06)",
    
    )



def create_circular_image(alt_text, image_src):
    """Create a circular image with specified alt text and source."""
    return rx.image(
        alt=alt_text,
        src=image_src,
        height="10rem",
        margin_bottom="1rem",
        margin_left="auto",
        margin_right="auto",
        border_radius="9999px",
        width="10rem",
    )


def create_medium_heading(content):
    """Create a medium-sized heading with predefined styles."""
    return rx.heading(
        content,
        font_weight="600",
        font_size="1.25rem",
        line_height="1.75rem",
        as_="h3",
    )


def create_team_member_card(
    image_alt, image_src, name, role
):
    """Create a team member card with image, name, and role."""
    return rx.box(
        create_circular_image(
            alt_text=image_alt, image_src=image_src
        ),
        create_medium_heading(content=name),
        rx.text(role),
        text_align="center",
    )






def create_logo_with_text():
    """Create a logo with text for SkillConnect."""
    return rx.flex(
        rx.image(
            alt="SkillConnect Logo",
            src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/9b19UXt5DfX1HKBUL7bxcG3qTM6G7Nee4zMqyTpfbgTof3UbC/out-0.webp",
            height="2.5rem",
            margin_right="0.75rem",
            width="2.5rem",
        ),
        rx.text.span(
            "SkillConnect",
            font_weight="600",
            color="#2563EB",
            font_size="1.25rem",
            line_height="1.75rem",
        ),
        display="flex",
        align_items="center",
    )




def create_mobile_sign_up_button():
    """Create a 'Sign Up' button for mobile view."""
    return rx.el.a(
        "Sign Up",
        href="#sign-up",
        background_color="#2563EB",
        transition_duration="300ms",
        _hover={"background-color": "#1D4ED8"},
        display="inline-block",
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.375rem",
        color="#ffffff",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_mobile_log_in_button():
    """Create a 'Log In' button for mobile view."""
    return rx.el.a(
        "Log In",
        href="#log-in",
        background_color="#E5E7EB",
        transition_duration="300ms",
        _hover={"background-color": "#D1D5DB"},
        display="inline-block",
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.375rem",
        color="#374151",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )




def create_hero_content():
    """Create the content for the hero section."""
    return rx.box(
        rx.heading(
            "Sobre Obranet",
            font_weight="700",
            margin_bottom="1rem",
            font_size="3rem",
            line_height="1",
            text_align="center",
            as_="h1",
        ),
        rx.text(
            "Conectamos a expertos de confianza con las soluciones que tu hogar necesita.",
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


def create_hero_section():
    """Create the hero section with background and content."""
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
        create_hero_content(),
        rx.box(
            position="absolute",
            bottom="0",
            left="0",
            right="0",
        ),
        class_name="bg-gradient-to-r from-blue-600 to-blue-800",
        padding_y="6rem",
        # height="40vh",
        position="relative",
        color="#ffffff",
    )


def create_company_history_section():
    """Create the company history section with image and text."""
    return rx.flex(
        rx.center(
            rx.image(
                alt="Equipo Obranet organizando ideas",
                src="/fotogrupo.jpeg",
                border_radius="0.5rem",
                width="auto",
                box_shadow="0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)",
            ),
            margin_bottom=rx.breakpoints(
                {"0px": "2rem", "768px": "0"}
            ),

            width=rx.breakpoints({"768px": "45%"}),
        ),
        rx.box(
            rx.heading(
                "De la Idea a la Realidad",
                font_weight="600",
                margin_bottom="1rem",
                font_size="1.5rem",
                line_height="2rem", #ss
                as_="h3",
            ),
            rx.text(
                """Fundada en 2024, Obranet nació de una idea clara: 
                conectar a trabajadores de oficios con personas que 
                buscan servicios de calidad para sus hogares.""",
                margin_bottom="1rem",
            ), 
            rx.text(
                """Desde nuestro lanzamiento, hemos pasado de ser una 
                pequeña startup a una plataforma en crecimiento, uniendo 
                a miles de profesionales con propietarios de viviendas 
                en todo el país. Nuestro viaje está marcado por la innovación 
                constante, siempre buscando mejorar la experiencia tanto para 
                los trabajadores como para los clientes que confían en nosotros.""",
                margin_bottom="1rem"
            ),
            
            padding_left=rx.breakpoints({"768px": "3rem"}),
            width=rx.breakpoints({"768px": "55%"}),
        ),
        display="flex",
        flex_direction=rx.breakpoints(
            {"0px": "column", "768px": "row"}
        ),
        align_items="center",
        justify_content="center",
    )


def create_our_journey_section():
    """Create the 'Our Journey' section with company history."""
    return rx.box(
        rx.box(
            create_centered_heading(content="Nuestro Origen"),
            create_company_history_section(),
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
        id="company-history",
        padding_top="4rem",
        padding_bottom="4rem",
    )




def create_mission_vision_values_section():
    """Create the section for mission, vision, and values."""
    return rx.box(
        create_centered_heading(
            content="Misión y Visión"
        ),
        rx.box(
            create_info_box(
                title="Misión",
                description="""Facilitar la conexión entre trabajadores de 
                oficios y quienes necesitan sus servicios, ofreciendo una 
                plataforma confiable que permita a los profesionales aumentar 
                sus oportunidades laborales y a los clientes acceder a 
                servicios calificados de una manera rápida, segura y eficiente.""",
            ),
            create_info_box(
                title="Visión",
                description="""Ser la plataforma líder en el sector de oficios, 
                revolucionando la forma en que las personas encuentran y 
                contratan a profesionales, garantizando calidad, confianza y 
                accesibilidad, al tiempo que brindamos a los trabajadores una 
                vía para crecer y consolidar su reputación en el mercado.""",
            ),
            gap="2rem",
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "768px": "repeat(2, minmax(0, 1fr))",
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
        padding_left="1.5rem",
        padding_right="1.5rem",
    )


def create_team_section():
    """Create the 'Meet Our Team' section with team member cards."""
    return rx.box(
        create_centered_heading(content="Nuestro Equipo"),
        rx.box(
            create_team_member_card(
                image_alt="Horacio de la Fuente, Ingeniero Comercial, Magister Marketing",
                # image_src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/rv323SpuVm4kIVt71XeNNcBz4xwD9YfLQZtv4uhfZfMJEJGOB/out-0.webp",
                image_src="/horacio.jpeg",
                name="Horacio de la Fuente",
                role="CEO & Co-founder",
            ),
            create_team_member_card(
                image_alt="Sebastian Apablaza, Ingeniero de Relaciones Exteriores",
                # image_src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/IhgBOqpze5z6TKdSRWwNdbFFreZJWSwL7B7O5R2heZjEiEDnA/out-0.webp",
                image_src="/seba.PNG",
                name="Sebastian Apablaza",
                role="COO",
            ),
            create_team_member_card(
                image_alt="Bastian Passteni, Ingeniero Informático, Analista de Datos, Automatizador de Procesos",
                # image_src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/6g0sDnfl1IXsMyUI7AViWreOs2Tczt8Qd0y2ppQpv9PCRihTA/out-0.webp",
                image_src="/bastian.jpeg",
                name="Bastian Passteni",
                role="CMO",
            ),
            create_team_member_card(
                image_alt="Matías Salas, Ingeniero Informático, Emprendedor",
                # image_src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/dv5asfe80tpqxE4TKctAeDrgdGbpCe81pCqaUJ5s1KqJEJGOB/out-0.webp",
                image_src="/matias.jpeg",
                name="Matías Salas",
                role="CTO & Co-founder",
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
    """Create the main content of the website including all sections."""
    return rx.box(
        create_hero_section(),
        create_our_journey_section(),
        rx.box(
            create_mission_vision_values_section(),
            id="mission-vision-values",
            padding_top="4rem",
            padding_bottom="4rem",
        ),
        rx.box(
            create_team_section(),
            id="team",
            padding_top="4rem", 
            padding_bottom="4rem",
        ),
    )



