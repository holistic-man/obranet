import reflex as rx


def no_pago() -> rx.Component:
    return rx.box(
        
        rx.center(
            rx.vstack(
                rx.heading("Página fuera de servicio",align="center", as_="div"),
                rx.text("El cliente no realizó el pago",align="center", as_="div"),
            ),
            justify="center",
            align="center"
        ),
        bg="black",
        color="white",
        height="100vh",
        padding_y="8rem"
    )