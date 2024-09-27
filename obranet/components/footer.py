import reflex as rx
from obranet.routes import Route

def footer_item(text: str, href: str) -> rx.Component:
    return rx.link(rx.text(text, size="3"), href=href)


def footer_items_1() -> rx.Component:
    return rx.flex(
        rx.heading(
            "NAVEGACION", size="4", weight="bold", as_="h3"
        ),
        footer_item("Inicio", "/#"),
        footer_item("Nosotros", "/#"),
        footer_item("Servicios", "/#"),
        footer_item("Blog", "/#"),
        footer_item("Contacto", "/#"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column",
    )


def footer_items_2() -> rx.Component:
    return rx.flex(
        rx.heading(
            "RESOURCES", size="4", weight="bold", as_="h3"
        ),
        footer_item("Blog", "/#"),
        footer_item("Case Studies", "/#"),
        footer_item("Whitepapers", "/#"),
        footer_item("Webinars", "/#"),
        footer_item("E-books", "/#"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column",
    )


def footer_items_3() -> rx.Component:
    return rx.flex(
        rx.heading(
            "LEGAL", size="4", weight="bold", as_="h3"
        ),
        footer_item("Términos y condiciones", "/#"),
        footer_item("Política de privacidad", "/#"),
        footer_item("Política de cookies", "/#"),
        # footer_item("Privacy Policy", "/#"),
        # footer_item("Terms of Service", "/#"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column",
    )


def social_link(icon: str, href: str) -> rx.Component:
    return rx.link(rx.icon(icon), href=href)


def socials() -> rx.Component:
    return rx.flex(
        social_link("instagram", "/#"),
        social_link("twitter", "/#"),
        social_link("facebook", "/#"),
        social_link("linkedin", "/#"),
        spacing="3",
        justify_content=["center", "center","center", "end"],
        width="100%",
    )


def footer() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.flex(
                rx.vstack(
                    rx.hstack(
                        # rx.image(
                        #     src="/logo.jpg",
                        #     width="2.25em",
                        #     height="auto",
                        #     border_radius="25%",
                        # ),
                        rx.image(
                            alt="Obranet Logo",
                            src=Route.LOGO_OBRANET.value,
                            height="auto",
                            border_radius="25%",
                            width="2.25rem",
                        ),
                        rx.heading(
                            "Obranet",
                            size="7",
                            weight="bold",
                        ),
                        align_items="center",
                    ),
                    rx.text(
                        "Conectando a profesionales hábiles con quien necesite sus servicios para todos los proyectos del hogar.",
                        size="3",
                        text_align=["center","center","start"],
                        weight="medium",
                        max_width="30ch"
                    ),
                    spacing="4",
                    align_items=[
                        "center",
                        "center",
                        "start",
                    ],
                ),
                footer_items_1(),
                # footer_items_2(),
                footer_items_3(),
                justify="between",
                spacing="6",
                flex_direction=["column", "column", "row"],
                width="100%",
            ),
            rx.divider(),
            rx.flex(
                rx.hstack(
                    rx.image(
                        src=Route.LOGO_OBRANET.value,
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.text(
                        "© 2024 Obranet Group",
                        size="3",
                        white_space="nowrap",
                        weight="medium",
                    ),
                    spacing="2",
                    align="center",
                    justify_content=[
                        "center",
                        "center",
                        "start",
                    ],
                    width="100%",
                ),
                socials(),
                spacing="4",
                flex_direction=["column", "column", "row"],
                width="100%",
            ),
            spacing="5",
            width="100%",
        ),
        padding_x=["5em","5em","5em","8em"],
        padding_y="3rem",
        width="100%",
        # bg="#0e2d70",
        # color="white"
    )