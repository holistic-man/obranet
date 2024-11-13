import reflex as rx

def developed_by():
    return rx.center(
        rx.text(
            "Página diseñada y desarrollada por ",
            rx.text.strong("Adaptate IA"),
            ". Solicita la tuya ",
            rx.link("aquí.", href="https://www.instagram.com/adaptate.ia", is_external=True, color_scheme="sky"),
        ),
        padding="1rem",
        bg="black",
        color="white",
        text_align="center"
    )