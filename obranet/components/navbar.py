import reflex as rx
import obranet.styles.styles as styles
# from obranet.components.icon_link import icon_link
from obranet.routes import Route

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(
            text, 
            size="4", 
            weight="medium"
        ), 
        href=url,
    )

def navbar() -> rx.Component:
    return rx.flex(
        rx.flex(
            rx.flex(
                rx.image(
                    alt="Obranet Logo",
                    src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/9b19UXt5DfX1HKBUL7bxcG3qTM6G7Nee4zMqyTpfbgTof3UbC/out-0.webp",
                    height="2.5rem",
                    margin_right="0.75rem",
                    width="2.5rem",
                    border_radius="25%",
                ),
                rx.text.span(
                    "Obranet",
                    font_weight="600",
                    color="#2563EB",
                    font_size="1.25rem",
                    line_height="1.75rem",
                ),
                display="flex",
                align_items="center",
            ),
            rx.hstack(
                navbar_link("Inicio", "/#"),
                navbar_link("Servicios", "/#"),
                navbar_link("Nosotros", "/#"),
                navbar_link("Blog", "/#"),
                spacing="5",
                display=["none", "none", "flex", "flex", "flex"],
            ),
            rx.hstack(
                rx.button(
                    "Ingresar",
                    size="3",
                    variant="outline",
                    display=["none", "none", "flex", "flex", "flex"],
                    cursor="pointer"
                ),
                rx.button(
                    "Registrate", 
                    size="3",
                    cursor="pointer"
                ),
                rx.drawer.root(
                    rx.drawer.trigger(
                        rx.button(
                            rx.icon(tag="menu"),
                            variant="outline",
                            size="3",
                            
                        ),
                        display=["flex", "flex", "none", "none", "none"],
                        cursor="pointer",
                        # color=styles.Color.WHITE_COLOR.value
                    ),
                    rx.drawer.overlay(),
                    rx.drawer.portal(
                        rx.drawer.content(
                            rx.vstack(
                                rx.hstack(
                                    # rx.avatar(
                                    #     src="/naty_avatar.jpg", 
                                    #     size="9",
                                    #     fallback="Naty",
                                    #     # radius="full",
                                    #     # margin="1em",
                                    #     # border = "2px solid #3442BD"
                                    # ),
                                    rx.flex(
                                        rx.drawer.close(
                                            rx.box(
                                                rx.button(
                                                    rx.icon(tag="x"),
                                                    variant="ghost",
                                                    cursor="pointer",
                                                )
                                            )
                                        ),
                                        align_items="start",
                                    ),
                                    justify="end",
                                    width="100%"
                                ),
                                rx.heading(
                                    "Obranet"
                                ),
                                rx.text(
                                    """
                                    Texto de descripcion
                                    """,
                                ),
                                rx.vstack(
                                    navbar_link("Inicio", "/#"),
                                    navbar_link("Servicios", "/#"),
                                    navbar_link("Nosotros", "/#"),
                                    navbar_link("Blog", "/#"),

                                    rx.hstack(
                                        rx.button(
                                            "Ingresar",
                                            size="3",
                                            variant="outline",
                                            cursor="pointer"
                                        ),
                                        rx.button(
                                            "Registrate", 
                                            size="3",
                                            cursor="pointer"
                                        ),
                                    ),
                                    spacing="5",
                                    align_items="start",
                                    padding_y=styles.EMSize.DEFAULT.value,
                                ),
                                width="100%"
                            ),
                                
                            height="100%",
                            width="85%",
                            padding=styles.EMSize.LARGE.value,
                            background = "white"
                        )
                    ),
                    direction="left",
                ),
                spacing="4",
                justify="end",
            ),
            justify="between",
            align_items="center",
            width="100%"
        ),
        as_="nav",
        align="center",
        justify="between",
        padding=styles.EMSize.DEFAULT.value,
        border_bottom = "1px solid #dce1e4", 
        bg = "#ecf0f3",
        box_shadow= "0px 4px 6px rgba(0, 0, 0, 0.1)",
        position="sticky", 
        zIndex="1000", 
        top="0",
    )