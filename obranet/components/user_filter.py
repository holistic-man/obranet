import reflex as rx
from obranet.state.RegisterState import RegisterState

def create_label(text):
    """Create a label element with specific styling."""
    return rx.el.label(
        text,
        display="block",
        font_weight="500",
        margin_bottom="0.5rem",
        # color="#374151",
        font_size="0.875rem",
        line_height="1.25rem",
    )


def create_option(option_value, option_text):
    """Create an option element for a select input."""
    return rx.el.option(option_text, value=option_value)


def create_icon(alt_text, height, icon_tag, width):
    """Create an icon element with specified attributes."""
    return rx.icon(
        alt=alt_text,
        tag=icon_tag,
        height=height,
        width=width,
    )


def create_text_input(input_id, placeholder_text):
    """Create a text input element with specific styling and attributes."""
    return rx.el.input(
        id=input_id,
        placeholder=placeholder_text,
        type="text",
        border_width="1px",
        border_color="#D1D5DB",
        _focus={
            "border-color": "#6366F1",
            "outline-style": "none",
            "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
            "--ring-color": "#6366F1",
        },
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="0.5rem",
        width="100%",
        on_change=RegisterState.set_search,
        value=RegisterState.search,
    )


def create_small_icon(alt_text, icon_tag):
    """Create a small icon element with specific styling."""
    return rx.icon(
        alt=alt_text,
        tag=icon_tag,
        height="1.25rem",
        color="#9CA3AF",
        width="1.25rem",
    )


def create_icon_wrapper(icon_alt, icon_tag):
    """Create a wrapper for an icon with specific positioning."""
    return rx.flex(
        create_small_icon(
            alt_text=icon_alt, icon_tag=icon_tag
        ),
        position="absolute",
        display="flex",
        top="0",
        bottom="0",
        align_items="center",
        pointer_events="none",
        padding_right="0.75rem",
        right="0",
    )


def create_input_with_icon(
    input_id, placeholder_text, icon_alt, icon_tag
):
    """Create an input element with an accompanying icon."""
    return rx.box(
        create_text_input(
            input_id=input_id,
            placeholder_text=placeholder_text,
        ),
        create_icon_wrapper(
            icon_alt=icon_alt, icon_tag=icon_tag
        ),
        position="relative",
    )



def create_service_select():
    """Create a select input for service types."""
    return rx.el.select(
        create_option(
            option_value=True, option_text="Todos los Servicios"
        ),
        create_option(
            option_value="gasfiter",
            option_text="Gasfiter",
        ),
        create_option(
            option_value="plomero",
            option_text="Plomero",
        ),
        create_option(
            option_value="electricista",
            option_text="Electricista",
        ),
        create_option(
            option_value="pintor",
            option_text="Pintor",
        ),
        # create_option(
        #     option_value="graphic-design",
        #     option_text="Graphic Design",
        # ),
        # create_option(
        #     option_value="digital-marketing",
        #     option_text="Digital Marketing",
        # ),
        id="service",
        appearance="none",
        # background_color="#ffffff",
        border_width="1px",
        border_color="#D1D5DB",
        _focus={
            "border-color": "#6366F1",
            "outline-style": "none",
            "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
            "--ring-color": "#6366F1",
        },
        line_height="1.25",
        padding_right="1rem",
        padding_left="1rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="0.5rem",
        width="100%",
    )


def create_dropdown_arrow():
    """Create a dropdown arrow icon for select inputs."""
    return rx.flex(
        create_icon(
            alt_text="Dropdown arrow",
            height="1rem",
            icon_tag="chevron-down",
            width="1rem",
        ),
        position="absolute",
        display="flex",
        top="0",
        bottom="0",
        align_items="center",
        pointer_events="none",
        padding_left="0.5rem",
        padding_right="0.5rem",
        right="0",
        # color="#374151",
    )


def create_filter_section():
    """Create a section with filter inputs for service type, location, and search."""
    return rx.box(
        rx.box(
            # create_label(text="Tipo de Servicio"),
            # rx.box(
            #     create_service_select(),
            #     create_dropdown_arrow(),
            #     position="relative",
                
            # ),
            # rx.select.root(
            #     rx.select.trigger(
            #         placeholder="Todos los Servicios",
            #         width="100%",
            #     ),
            #     rx.select.content(
            #         rx.select.item(
            #             "Todlos los servicios", 
            #             value="all"
            #         ),
            #         rx.select.item(
            #             "Pintor", 
            #             value="pintor"
            #         ),
            #          rx.select.item(
            #              "Gasfiter", 
            #             value="gasfiter"
            #         ),
            #         rx.select.item(
            #             "Jardinero", 
            #             value="jardinero"
            #         ),
            #         rx.select.item(
            #             "Electricista", 
            #             value="electricista"
            #         ),
            #         rx.select.item(
            #             "Otro (Detalla en la descripción)", 
            #             value="otro"
            #         ),
            #         side="bottom"
            #     ),
            #     value=RegisterState.service,
            #     on_change=RegisterState.set_service,
            #     width="100%",
            #     name="service",        
            # ),  
            # rx.select(
            #     ["pintor", "jardinero", "electricista","gasfiter"],
            #     placeholder="Filtrar por tipo de servicio",
            #     on_change=RegisterState.set_service,
            # ),
        ),
        rx.box(
            create_label(text="Ubicación"),
            create_input_with_icon(
                input_id="location",
                placeholder_text="Ingresa región o comuna",
                icon_alt="Location pin",
                icon_tag="map-pin",
            ),
        ),
        rx.box(
            create_label(text="Búsqueda"),
            create_input_with_icon(
                input_id="search",
                placeholder_text="Busca nombre o servicio",
                icon_alt="Search icon",
                icon_tag="search",
            ),
        ),
        gap="1.5rem",
        display="grid",
        grid_template_columns=rx.breakpoints(
            {
                "0px": "repeat(1, minmax(0, 1fr))",
                "768px": "repeat(3, minmax(0, 1fr))",
            }
        ),
    )


def create_apply_filters_button():
    """Create a styled 'Apply Filters' button."""
    return rx.el.button(
        " Aplicar Filtros ",
        class_name="md:flex-grow-0 transform",
        background_color="#4F46E5",
        transition_duration="300ms",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
        flex_grow="1",
        _focus={
            "outline-style": "none",
            "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
            "--ring-color": "#6366F1",
            "--ring-opacity": "0.5",
        },
        font_weight="700",
        _hover={
            "background-color": "#4338CA",
            "transform": "scale(1.05)",
        },
        padding_left="1.5rem",
        padding_right="1.5rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="0.5rem",
        color="#ffffff",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        on_click=RegisterState.apply_filters,
        loading=RegisterState.is_loading
    )


def create_clear_filters_button():
    """Create a styled 'Clear Filters' button."""
    return rx.el.button(
        " Limpiar Filtros ",
        class_name="md:flex-grow-0",
        background_color="#E5E7EB",
        transition_duration="300ms",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
        flex_grow="1",
        _focus={
            "outline-style": "none",
            "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
            "--ring-color": "#9CA3AF",
            "--ring-opacity": "0.5",
        },
        font_weight="700",
        _hover={"background-color": "#D1D5DB"},
        padding_left="1.5rem",
        padding_right="1.5rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="0.5rem",
        color="#374151",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        on_click=RegisterState.clear_filters,
        loading=RegisterState.is_clearing_filters
    )


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
                rx.select.root(
                    rx.select.trigger(
                        placeholder="Todos los Servicios",
                        width="100%",
                    ),
                    rx.select.content(
                        rx.select.item(
                            "Todos los servicios", 
                            value="all"
                        ),
                        rx.select.item(
                            "Pintor", 
                            value="pintor"
                        ),
                        rx.select.item(
                            "Gasfiter", 
                            value="gasfiter"
                        ),
                        rx.select.item(
                            "Jardinero", 
                            value="jardinero"
                        ),
                        rx.select.item(
                            "Electricista", 
                            value="electricista"
                        ),
                        rx.select.item(
                            "Otro (Detalla en la descripción)", 
                            value="otro"
                        ),
                        side="bottom"
                    ),
                    value=RegisterState.service_filter,
                    on_change=RegisterState.set_service_filter,
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
                rx.select.root(
                    rx.select.trigger(
                        placeholder="Selecciona la Comuna",
                        width="100%",
                    ),
                    rx.select.content(
                        rx.select.item(
                            "Todas las comunas", 
                            value="all_location"
                        ),
                        rx.select.item(
                            "Santiago", 
                            value="santiago"
                        ),
                        rx.select.item(
                            "Independencia", 
                            value="independencia"
                        ),
                        rx.select.item(
                            "Recoleta", 
                            value="recoleta"
                        ),
                        rx.select.item(
                            "Huechuraba", 
                            value="huechuraba"
                        ),
                        rx.select.item(
                            "Conchalí", 
                            value="conchali"
                        ),
                        side="bottom"
                    ),
                    value=RegisterState.location_filter,
                    on_change=RegisterState.set_location_filter,
                    width="100%",
                    size="3",
                    name="location",        
                ),  
                # rx.input(
                #     rx.input.slot(
                #         rx.icon(tag="search"),
                #         position="right",
                #     ),
                #     placeholder="Ingresa comuna",
                #     on_change=RegisterState.set_location,
                #     value=RegisterState.location,
                #     width="100%",
                #     size="3",
                #     name="location"
                # )
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
                    on_change=RegisterState.set_search_filter,
                    value=RegisterState.search_filter,
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
                on_click=RegisterState.apply_filters,
                loading=RegisterState.is_applying_filters,
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
                on_click=RegisterState.clear_filters,
                loading=RegisterState.is_clearing_filters,
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
