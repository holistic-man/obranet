import reflex as rx
from obranet.models import Registrado

def user_detail_link(user: Registrado):
    if user is None or user.service is None or user.name is None:
        return rx.fragment()
    user_detail_url = f"/servicios/{user.service}/{user.name}"
    return rx.link(
        rx.button(
            "Ver perfil",
            width="100%",
            cursor="pointer",
            size="3"
        ),
        href=user_detail_url,
        width="100%"
    )
 

def user_info(user:Registrado) -> rx.Component:
    return rx.box(
        # rx.text(user.name),
        # rx.text(user.email),
        # rx.text(user.service),
        # rx.text(user.description),
        rx.flex(
            rx.cond(
                user.photo,
                rx.image(
                    src=user.photo,
                    alt=f"Foto de perfil de {user.name} en Obranet",
                    height="4rem",
                    margin_right="1rem",
                    border_radius="9999px",
                    width="4rem",
                ),
                rx.image(
                    src="/user_generico.jpeg",
                    alt=f"Foto de perfil generico en Obranet",
                    height="4rem",
                    margin_right="1rem",
                    border_radius="9999px",
                    width="4rem",
                ),
            ),
            # rx.image(
            #     src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/2fpH0jjntek0oEHoEqkVbyn6tvucNhd4fVAA2EHnrQqpUVGnA/out-0.webp",
            #     # src=user.photo,
            #     alt=f"Foto de perfil de {user.name} en Obranet",
            #     height="4rem",
            #     margin_right="1rem",
            #     border_radius="9999px",
            #     width="4rem",
            # ),
            rx.box(
                rx.heading(
                    user.name,
                    font_weight="600",
                    font_size="1.25rem",
                    line_height="1.75rem",
                    as_="h2",
                ),
                rx.text(
                    rx.icon(
                        tag='contact',
                        height="1rem",
                        display="inline-block",
                        margin_right="0.5rem",
                        width="1rem",
                    ),
                    user.service
                ),
                # create_colored_text(
                #     text_color="#4B5563",
                #     content="Software Engineer",
                # ),
                rx.text(
                    rx.icon(
                        tag='map-pin',
                        height="1rem",
                        display="inline-block",
                        margin_right="0.5rem",
                        width="1rem",
                    ),
                    user.location,
                    color="#6B7280",
                    font_size="0.875rem",
                    line_height="1.25rem",
                ),
            ),
            display="flex",
            align_items="center",
            # margin_bottom="1rem",
            padding="1rem"
        ),
        rx.flex(
            rx.vstack(
                rx.heading("Sobre mi"),
                rx.text(
                    user.description,
                    overflow="hidden",
                    display="-webkit-box",
                    style={
                        "-webkit-line-clamp": "3",
                        "-webkit-box-orient": "vertical",
                    },
                ),
                align_items="stretch",
                height="100%",
            ),
            user_detail_link(user),
            direction="column",
            justify="space-between",
            height="200px",  # Ajusta esta altura según tus necesidades
            padding="1em",
        ),
        # background_color="black",
        overflow="hidden",
        width="100%",
        # border="1px solid",
        border_radius="0.5rem",
        box_shadow = rx.color_mode_cond(
            light="0 0 10px rgba(0, 0, 0, 0.2)",
            dark="0 0 10px rgba(255, 255, 255, 0.2)"
        ),
    )




def create_colored_text(text_color, content):
    """Create a text component with specified color and content."""
    return rx.text(content, color=text_color)


def create_profile_info():
    """Create a box component containing profile information including name, job title, and location."""
    return rx.box(
        rx.heading(
            "John Doe",
            font_weight="600",
            font_size="1.25rem",
            line_height="1.75rem",
            as_="h2",
        ),
        create_colored_text(
            text_color="#4B5563",
            content="Software Engineer",
        ),
        rx.text(
            "San Francisco, CA",
            color="#6B7280",
            font_size="0.875rem",
            line_height="1.25rem",
        ),
    )


def create_profile_header():
    """Create a flex component with profile image and information."""
    return rx.flex(
        rx.image(
            src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/2fpH0jjntek0oEHoEqkVbyn6tvucNhd4fVAA2EHnrQqpUVGnA/out-0.webp",
            alt="Circular profile image of a person with brown hair and a friendly smile",
            height="4rem",
            margin_right="1rem",
            border_radius="9999px",
            width="4rem",
        ),
        create_profile_info(),
        display="flex",
        align_items="center",
        margin_bottom="1rem",
    )


def create_view_profile_button():
    """Create a styled 'View Profile' button component."""
    return rx.el.button(
        "View Profile",
        background_color="#3B82F6",
        transition_duration="300ms",
        _hover={"background-color": "#2563EB"},
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.5rem",
        color="#ffffff",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
        width="100%",
    )


def create_profile_card():
    """Create a complete profile card component with header, about section, and view profile button."""
    return rx.box(
        create_profile_header(),
        rx.box(
            rx.heading(
                "About",
                font_weight="600",
                margin_bottom="0.5rem",
                as_="h3",
                size="4",
            ),
            create_colored_text(
                text_color="#374151",
                content="Passionate software engineer with 5+ years of experience in developing scalable web applications. Skilled in React, Node.js, and cloud technologies.",
            ),
            margin_bottom="1rem",
        ),
        create_view_profile_button(),
        background_color="#ffffff",
        max_width="28rem",
        margin_left="auto",
        margin_right="auto",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def render_profile_page():
    """Render the main profile page containing the profile card."""
    return rx.fragment(rx.box(create_profile_card()))
