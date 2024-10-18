import reflex as rx
from obranet.backend.states import UserListState
import obranet.constants as const 

def user_filter():
    return rx.box(
        rx.heading(
            "Encuentra a tu profesional perfecto",
            font_weight="600",
            margin_bottom="1.5rem",
            font_size="1.5rem",
            line_height="2rem",
            # color="#374151",
            as_="h2",
        ),
        # create_filter_section(),
        rx.flex(
            rx.box(
                rx.text(
                    "Servicio",
                    display="block",
                    font_weight="500",
                    margin_bottom="0.5rem",
                    # color="#374151",
                    font_size="0.875rem",
                    line_height="1.25rem",
                ),
                rx.select(
                    const.SERVICES,
                    placeholder="Todos los Servicios",
                    value=UserListState.service_filter,
                    on_change=UserListState.set_service_filter,
                    width="100%",
                    size="3",
                    name="service",  
                ),
            ),
            
            rx.box(
                rx.text(
                    "Ubicación",
                    display="block",
                    font_weight="500",
                    margin_bottom="0.5rem",
                    # color="#374151",
                    font_size="0.875rem",
                    line_height="1.25rem",
                ),
                rx.select(
                    const.COMUNAS,
                    placeholder="Selecciona la comuna",
                    name="location",
                    value=UserListState.location_filter,
                    on_change=UserListState.set_location_filter,
                    width="100%",
                    size="3",
                ),
            ),
            rx.box(
                rx.text(
                    "Búsqueda",
                    display="block",
                    font_weight="500",
                    margin_bottom="0.5rem",
                    # color="#374151",
                    font_size="0.875rem",
                    line_height="1.25rem",
                ),
                rx.input(
                    rx.input.slot(
                        rx.icon(tag="search"),
                        position="right",
                    ),
                    placeholder="Busca por nombre o servicio",
                    on_change=UserListState.set_search_filter,
                    value=UserListState.search_filter,
                    width="100%",
                    size="3",
                    name="search"
                )
            ),
            width="100%",
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "768px": "repeat(3, minmax(0, 1fr))",
                }
            ),
            gap="1rem",
            margin_top="1.5rem",
        ),
        rx.flex(
            rx.button(
                "Aplicar filtros", 
                font_weight="700",
                cursor="pointer",
                size="3",
                transition_duration="300ms",
                transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
                transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
                on_click=UserListState.apply_filters,
                loading=UserListState.is_applying_filters,
            ),
            rx.button(
                "Limpiar filtros", 
                font_weight="700",
                cursor="pointer",
                size="3",
                variant="soft",
                color="#374151",
                background="#E5E7EB",
                _hover={"background-color": "#D1D5DB"},
                transition_duration="300ms",
                transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
                transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
                on_click=UserListState.clear_filters,
                loading=UserListState.is_clearing_filters,
            ),
            width="100%",
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "768px": "repeat(2, minmax(0, 1fr))",
                }
            ),
            gap="1rem",
            margin_top="1.5rem",
        ),
        # background_color="#ffffff",
        margin_y="2rem",
        border_radius="0.5rem",
        # box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
        width="100%"
    )
