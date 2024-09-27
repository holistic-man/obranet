import reflex as rx
from obranet.models import Registrado
from obranet.routes import Route
from obranet.state.RegisterState import RegisterState





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
        rx.box(
            rx.box(
                rx.image(
                    alt="Imagen de perfil de usuario registrado en Obranet",
                    src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/wlez7bzBYjVoQKsMR7g3GOBvjA1X9Ns9x9MJo0Zaef5Gz98mA/out-0.webp",
                    height=rx.breakpoints(
                        {"0px": "12rem", "768px": "100%"}
                    ),
                    object_fit="cover",
                    width=rx.breakpoints(
                        {"0px": "100%", "768px": "12rem"}
                    ),
                    border="3px solid"
                )       
            ),
            rx.box(

                rx.text(
                    user.name,
                    font_weight="700",
                    # line_height=rx.breakpoints(
                    #     {"0px": "2.25rem", "640px": "2.5rem"}
                    # ),
                    margin_top="0.5rem",
                    # font_size=rx.breakpoints(
                    #     {"0px": "1.875rem", "640px": "2.25rem"}
                    # ),
                    # color="#111827",
                    letter_spacing="-0.025em",
                    # as_="h2",
                ),
                rx.text(
                        rx.icon(
                            tag='contact',
                            height="1rem",
                            display="inline-block",
                            margin_right="0.5rem",
                            width="1rem",
                        ),
                        user.service,
                       
                    ),
                    rx.text(
                        rx.icon(
                            tag='map-pin',
                            height="1rem",
                            display="inline-block",
                            margin_right="0.5rem",
                            width="1rem",
                        ),
                        user.location,
                    ),
                padding="1em",
            ),
            display=rx.breakpoints({"768px": "flex"}),
        ),
        rx.flex(
            rx.vstack(
                rx.heading("Sobre mi"),
                rx.text(
                    user.description,
                    overflow="hidden",
                    text_overflow="ellipsis",
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
        border_radius="0.75rem",
        border="1px solid"
        # box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
    )





