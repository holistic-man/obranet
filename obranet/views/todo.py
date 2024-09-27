import reflex as rx

def create_icon(icon_name):
    """Create an icon component with specified tag and styling."""
    return rx.icon(
        tag=icon_name,
        height="1.25rem",
        margin_right="0.5rem",
        width="1.25rem",
    )


def create_colored_span(text_content):
    """Create a span element with specified text content and color."""
    return rx.text.span(text_content, color="#4B5563")


def create_avatar_image(alt_text, image_src):
    """Create a circular avatar image component with specified source and alt text."""
    return rx.image(
        src=image_src,
        alt=alt_text,
        height="2rem",
        margin_right="0.5rem",
        border_radius="9999px",
        width="2rem",
    )


def create_bold_span(text_content):
    """Create a span element with bold text content."""
    return rx.text.span(text_content, font_weight="600")





def create_gray_text(text_content):
    """Create a text element with gray color."""
    return rx.text(text_content, color="#4B5563")


def create_contact_info():
    """Create a contact information section with location and phone number."""
    return rx.box(
        rx.flex(
            create_icon(icon_name="map-pin"),
            create_colored_span(
                text_content="New York, NY"
            ),
            display="flex",
            align_items="center",
            margin_bottom="0.5rem",
        ),
        rx.flex(
            create_icon(icon_name="phone"),
            create_colored_span(
                text_content="(123) 456-7890"
            ),
            display="flex",
            align_items="center",
        ),
        margin_top="1rem",
    )


def create_profile_details():
    """Create a profile details section with name, job title, contact info, and description."""
    return rx.box(
        rx.heading(
            "John Doe",
            font_weight="700",
            font_size="1.5rem",
            line_height="2rem",
            color="#111827",
            as_="h1",
        ),
        rx.text(
            "Software Engineer",
            color="#4B5563",
            font_size="1.25rem",
            line_height="1.75rem",
        ),
        create_contact_info(),
        rx.text(
            "Experienced software engineer with a passion for creating efficient and scalable web applications. Specialized in JavaScript, React, and Node.js.",
            margin_top="1rem",
            color="#4B5563",
        ),
        padding="2rem",
    )


def create_profile_header():
    """Create a profile header with a large image and profile details."""
    return rx.box(
        rx.box(
            rx.image(
                src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/ABPCPqakr57FDJJsCaWOaBeIsZUfs1IV5NvJImRAILf3BlfNB/out-0.webp",
                alt="Professional headshot of a smiling person with short dark hair in business attire",
                height="12rem",
                object_fit="cover",
                width=rx.breakpoints(
                    {"0px": "100%", "768px": "12rem"}
                ),
            ),
            class_name="md:flex-shrink-0",
        ),
        create_profile_details(),
        display=rx.breakpoints({"768px": "flex"}),
    )





def create_profile_card():
    return rx.box(
        rx.box(
            create_profile_header(),
            background_color="#ffffff",
            max_width="56rem",
            margin_left="auto",
            margin_right="auto",
            overflow="hidden",
            border_radius="0.5rem",
            box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
        ),
        background_color="#F3F4F6",
        min_height="100vh",
        padding_top="2rem",
        padding_bottom="2rem",
    )


def render_profile_page():
    """Render the entire profile page with all components."""
    return rx.fragment(rx.box(create_profile_card()))