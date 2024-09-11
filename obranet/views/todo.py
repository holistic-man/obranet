import reflex as rx

def create_link_element(href, rel):
    """Create a link element with the specified href and rel attributes."""
    return rx.el.link(rel=rel, href=href)


def create_anchor_element(
    hover_style, color, href, content
):
    """Create an anchor element with specified hover style, color, href, and content."""
    return rx.el.a(
        content, href=href, _hover=hover_style, color=color
    )


def create_list_item_with_anchor(
    hover_style, color, href, content
):
    """Create a list item containing an anchor element with specified styles and content."""
    return rx.el.li(
        create_anchor_element(
            hover_style=hover_style,
            color=color,
            href=href,
            content=content,
        )
    )


def create_icon(alt_text, icon_tag):
    """Create an icon with specified alt text and tag, with default size of 1.5rem."""
    return rx.icon(
        alt=alt_text,
        tag=icon_tag,
        height="1.5rem",
        width="1.5rem",
    )


def create_styled_heading(
    heading_level, font_size, margin_bottom, content
):
    """Create a styled heading with specified level, font size, margin, and content."""
    return rx.heading(
        content,
        font_weight="600",
        margin_bottom=margin_bottom,
        font_size=font_size,
        line_height="1.75rem",
        as_=heading_level,
    )


def create_styled_paragraph(content):
    """Create a styled paragraph with default margin and font size."""
    return rx.text(
        content,
        margin_bottom="2rem",
        font_size="1.25rem",
        line_height="1.75rem",
    )


def create_centered_heading(content):
    """Create a centered heading with default styles for section titles."""
    return rx.heading(
        content,
        font_weight="600",
        margin_bottom="3rem",
        font_size="1.875rem",
        line_height="2.25rem",
        text_align="center",
        as_="h2",
    )


def create_large_centered_icon(alt_text, icon_tag):
    """Create a large centered icon with specified alt text and tag."""
    return rx.icon(
        alt=alt_text,
        tag=icon_tag,
        height="4rem",
        margin_bottom="1rem",
        margin_left="auto",
        margin_right="auto",
        width="4rem",
    )


def create_colored_text(color, content):
    """Create a text element with specified color and content."""
    return rx.text(content, color=color)


def create_feature_box(
    icon_alt, icon_tag, title, description
):
    """Create a feature box with an icon, title, and description."""
    return rx.box(
        create_large_centered_icon(
            alt_text=icon_alt, icon_tag=icon_tag
        ),
        create_styled_heading(
            heading_level="h3",
            font_size="1.25rem",
            margin_bottom="0.5rem",
            content=title,
        ),
        create_colored_text(
            color="#4B5563", content=description
        ),
        text_align="center",
    )


def create_centered_image(alt_text, image_src):
    """Create a centered image with specified alt text and source."""
    return rx.image(
        alt=alt_text,
        src=image_src,
        height="5rem",
        margin_bottom="1rem",
        margin_left="auto",
        margin_right="auto",
        width="5rem",
    )


def create_responsive_heading(content):
    """Create a responsive heading with different sizes for mobile and desktop."""
    return rx.heading(
        content,
        font_weight="600",
        font_size=rx.breakpoints(
            {"0px": "1.125rem", "640px": "1.25rem"}
        ),
        line_height=rx.breakpoints(
            {"0px": "1.75rem", "640px": "1.75rem"}
        ),
        as_="h3",
    )


def create_service_card(image_alt, image_src, service_name):
    """Create a service card with an image and service name, including hover effects."""
    return rx.box(
        create_centered_image(
            alt_text=image_alt, image_src=image_src
        ),
        create_responsive_heading(content=service_name),
        class_name="transform",
        background_color="#ffffff1a",
        transition_duration="300ms",
        _hover={"transform": "scale(1.05)"},
        padding=rx.breakpoints(
            {"0px": "1.5rem", "640px": "2rem"}
        ),
        border_radius="0.5rem",
        box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
        text_align="center",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_colored_icon(alt_text, icon_color, icon_tag):
    """Create a colored icon with specified alt text, color, and tag."""
    return rx.icon(
        alt=alt_text,
        tag=icon_tag,
        height="2rem",
        margin_right="1rem",
        color=icon_color,
        width="2rem",
    )


def create_info_box(title, description):
    """Create an information box with a title and description."""
    return rx.box(
        create_styled_heading(
            heading_level="h3",
            font_size="1.25rem",
            margin_bottom="0.5rem",
            content=title,
        ),
        create_colored_text(
            color="#4B5563", content=description
        ),
    )


def create_styled_button(
    hover_style, bg_color, href, content
):
    """Create a styled button with hover effects, background color, and link."""
    return rx.el.a(
        content,
        href=href,
        background_color=bg_color,
        transition_duration="300ms",
        font_weight="600",
        _hover=hover_style,
        padding_left="1.5rem",
        padding_right="1.5rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="0.375rem",
        color="#ffffff",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_social_media_link(href, icon_alt, icon_tag):
    """Create a social media link with an icon."""
    return rx.el.a(
        create_icon(alt_text=icon_alt, icon_tag=icon_tag),
        href=href,
        target="_blank",
        rel="noopener noreferrer",
        _hover={"color": "#ffffff"},
        color="#9CA3AF",
    )


# def create_logo_with_text():
#     """Create a logo with text for SkillConnect."""
#     return rx.flex(
#         rx.image(
#             alt="SkillConnect Logo",
#             src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/9b19UXt5DfX1HKBUL7bxcG3qTM6G7Nee4zMqyTpfbgTof3UbC/out-0.webp",
#             height="2.5rem",
#             margin_right="0.75rem",
#             width="2.5rem",
#         ),
#         rx.text.span(
#             "SkillConnect",
#             font_weight="600",
#             color="#2563EB",
#             font_size="1.25rem",
#             line_height="1.75rem",
#         ),
#         display="flex",
#         align_items="center",
#     )


# def create_sign_up_button():
#     """Create a sign up button with default styles."""
#     return rx.el.a(
#         "Sign Up",
#         href="#sign-up",
#         background_color="#2563EB",
#         transition_duration="300ms",
#         _hover={"background-color": "#1D4ED8"},
#         padding_left="1rem",
#         padding_right="1rem",
#         padding_top="0.5rem",
#         padding_bottom="0.5rem",
#         border_radius="0.375rem",
#         color="#ffffff",
#         transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
#         transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
#     )


# def create_log_in_button():
#     """Create a log in button with default styles."""
#     return rx.el.a(
#         "Log In",
#         href="#log-in",
#         background_color="#E5E7EB",
#         transition_duration="300ms",
#         _hover={"background-color": "#D1D5DB"},
#         padding_left="1rem",
#         padding_right="1rem",
#         padding_top="0.5rem",
#         padding_bottom="0.5rem",
#         border_radius="0.375rem",
#         color="#374151",
#         transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
#         transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
#     )


# def create_navigation_bar():
#     """Create the main navigation bar with logo, menu items, and action buttons."""
#     return rx.flex(
#         create_logo_with_text(),
#         rx.box(
#             rx.list(
#                 create_list_item_with_anchor(
#                     hover_style={"color": "#2563EB"},
#                     color="#4B5563",
#                     href="#how-it-works",
#                     content="How It Works",
#                 ),
#                 create_list_item_with_anchor(
#                     hover_style={"color": "#2563EB"},
#                     color="#4B5563",
#                     href="#services",
#                     content="Services",
#                 ),
#                 create_list_item_with_anchor(
#                     hover_style={"color": "#2563EB"},
#                     color="#4B5563",
#                     href="#about-us",
#                     content="About Us",
#                 ),
#                 create_list_item_with_anchor(
#                     hover_style={"color": "#2563EB"},
#                     color="#4B5563",
#                     href="#contact",
#                     content="Contact",
#                 ),
#                 display="flex",
#                 column_gap="1.5rem",
#             ),
#             display=rx.breakpoints(
#                 {"0px": "none", "768px": "flex"}
#             ),
#         ),
#         rx.box(
#             create_sign_up_button(),
#             create_log_in_button(),
#             display=rx.breakpoints(
#                 {"0px": "none", "768px": "flex"}
#             ),
#             column_gap="1rem",
#         ),
#         rx.box(
#             rx.el.button(
#                 create_icon(
#                     alt_text="Menu", icon_tag="menu"
#                 ),
#                 id="menu-toggle",
#                 _focus={"outline-style": "none"},
#                 _hover={"color": "#2563EB"},
#                 color="#4B5563",
#             ),
#             display=rx.breakpoints({"768px": "none"}),
#         ),
#         display="flex",
#         align_items="center",
#         justify_content="space-between",
#     )


# def create_mobile_sign_up_button():
#     """Create a sign up button for mobile view."""
#     return rx.el.a(
#         "Sign Up",
#         href="#sign-up",
#         background_color="#2563EB",
#         transition_duration="300ms",
#         _hover={"background-color": "#1D4ED8"},
#         display="inline-block",
#         padding_left="1rem",
#         padding_right="1rem",
#         padding_top="0.5rem",
#         padding_bottom="0.5rem",
#         border_radius="0.375rem",
#         color="#ffffff",
#         transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
#         transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
#     )


# def create_mobile_log_in_button():
#     """Create a log in button for mobile view."""
#     return rx.el.a(
#         "Log In",
#         href="#log-in",
#         background_color="#E5E7EB",
#         transition_duration="300ms",
#         _hover={"background-color": "#D1D5DB"},
#         display="inline-block",
#         padding_left="1rem",
#         padding_right="1rem",
#         padding_top="0.5rem",
#         padding_bottom="0.5rem",
#         border_radius="0.375rem",
#         color="#374151",
#         transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
#         transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
#     )


# def     create_mobile_menu():
#     """Create the mobile menu with navigation items and action buttons."""
#     return rx.list(
#         create_list_item_with_anchor(
#             hover_style={"color": "#2563EB"},
#             color="#4B5563",
#             href="#how-it-works",
#             content="How It Works",
#         ),
#         create_list_item_with_anchor(
#             hover_style={"color": "#2563EB"},
#             color="#4B5563",
#             href="#services",
#             content="Services",
#         ),
#         create_list_item_with_anchor(
#             hover_style={"color": "#2563EB"},
#             color="#4B5563",
#             href="#about-us",
#             content="About Us",
#         ),
#         create_list_item_with_anchor(
#             hover_style={"color": "#2563EB"},
#             color="#4B5563",
#             href="#contact",
#             content="Contact",
#         ),
#         rx.el.li(create_mobile_sign_up_button()),
#         rx.el.li(create_mobile_log_in_button()),
#         display="flex",
#         flex_direction="column",
#         gap="1rem",
#     )


def create_responsive_header():
    """Create a responsive header with navigation and mobile menu."""
    return rx.box(
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


def create_hire_professional_button():
    """Create a button for hiring a professional."""
    return rx.el.a(
        "Hire a Professional",
        href="#hire",
        background_color="#ffffff",
        transition_duration="300ms",
        font_weight="600",
        _hover={"background-color": "#F3F4F6"},
        padding_left="2rem",
        padding_right="2rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="9999px",
        color="#2563EB",
        text_align="center",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_offer_services_button():
    """Create a button for offering services."""
    return rx.el.a(
        "Offer Your Services",
        href="#offer-services",
        background_color="transparent",
        border_width="2px",
        border_color="#ffffff",
        transition_duration="300ms",
        font_weight="600",
        _hover={
            "background-color": "#ffffff",
            "color": "#2563EB",
        },
        padding_left="2rem",
        padding_right="2rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="9999px",
        text_align="center",
        color="#ffffff",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_hero_content():
    """Create the main content for the hero section."""
    return rx.box(
        rx.heading(
            "Transform Your Home with Skilled Professionals",
            font_weight="700",
            line_height="1",
            margin_bottom="1.5rem",
            font_size="3rem",
            as_="h1",
        ),
        create_styled_paragraph(
            content="Connect with trusted experts for all your home improvement needs. Quality work, guaranteed satisfaction."
        ),
        rx.flex(
            create_hire_professional_button(),
            create_offer_services_button(),
            display="flex",
            flex_direction=rx.breakpoints(
                {"0px": "column", "640px": "row"}
            ),
            gap=rx.breakpoints(
                {"0px": "1rem", "640px": "0"}
            ),
            column_gap=rx.breakpoints({"640px": "1rem"}),
        ),
        margin_bottom=rx.breakpoints(
            {"0px": "2rem", "768px": "0"}
        ),
        width=rx.breakpoints({"768px": "50%"}),
    )


def create_hero_section():
    """Create the complete hero section with content and image."""
    return rx.flex(
        create_hero_content(),
        rx.box(
            rx.image(
                alt="Happy homeowner with skilled professional working on home improvement project",
                src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/HkfM7iZdVZRVeUfDCkf88xNqNo4U1J0Ny4N6AoN9fkxLn4UbC/out-0.webp",
                border_radius="0.5rem",
                box_shadow="0 25px 50px -12px rgba(0, 0, 0, 0.25)",
            ),
            width=rx.breakpoints({"768px": "50%"}),
        ),
        display="flex",
        flex_direction=rx.breakpoints(
            {"0px": "column", "768px": "row"}
        ),
        align_items="center",
        justify_content="space-between",
    )


def create_hero_container():
    """Create the container for the hero section with background and styling."""
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
        rx.box(
            create_hero_section(),
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
        ),
        rx.box(
            position="absolute",
            bottom="0",
            left="0",
            right="0",
        ),
        class_name="bg-gradient-to-r from-blue-600 to-blue-800",
        padding_top="8rem",
        padding_bottom="8rem",
        position="relative",
        color="#ffffff",
    )


def create_how_it_works_section():
    """Create the 'How SkillConnect Works' section with steps."""
    return rx.box(
        create_centered_heading(
            content="How SkillConnect Works"
        ),
        rx.box(
            create_feature_box(
                icon_alt="Create Profile Icon",
                icon_tag="user-plus",
                title="Create a Profile",
                description="Showcase your skills and experience to potential clients",
            ),
            create_feature_box(
                icon_alt="Search Icon",
                icon_tag="search",
                title="Search for Services",
                description="Find the right professional for your specific needs",
            ),
            create_feature_box(
                icon_alt="Connect Icon",
                icon_tag="message-square",
                title="Connect and Hire",
                description="Communicate directly and hire with confidence",
            ),
            gap="2rem",
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "768px": "repeat(3, minmax(0, 1fr))",
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


def create_view_all_services_button():
    """Create a button to view all services."""
    return rx.el.a(
        "View All Services",
        href="#all-services",
        background_color="#ffffff",
        transition_duration="300ms",
        font_weight="600",
        _hover={
            "background-color": "#F3F4F6",
            "box-shadow": "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
        },
        display="inline-block",
        padding_left="2rem",
        padding_right="2rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="9999px",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
        color="#2563EB",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_featured_services_section():
    """Create the featured services section with service cards."""
    return rx.box(
        create_centered_heading(
            content="Featured Services"
        ),
        rx.box(
            create_service_card(
                image_alt="Professional painter with brush and paint bucket",
                image_src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/o5ekD5edTsg4eJ8PIzF0vfnhNmFU9UZhaB4ZAseLMawVfvp2E/out-0.webp",
                service_name="Painters",
            ),
            create_service_card(
                image_alt="Plumber fixing a sink with wrench",
                image_src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/mDaVHsO8RFqhIZ4iLGd96FfPxsOR3PN4xzQkZfBzNnt6fN1mA/out-0.webp",
                service_name="Plumbers",
            ),
            create_service_card(
                image_alt="Electrician working on electrical panel",
                image_src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/1B0pIsZ0VzZSGhL0ORLSwtAarJqI8lCJMXsmXFQi86iefmaTA/out-0.webp",
                service_name="Electricians",
            ),
            create_service_card(
                image_alt="Gardener planting flowers in a garden",
                image_src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/JsRveV3NtWXgYC7MMXhVWTjyRIZccxYgkFfe5Hj7N0t1fbqNB/out-0.webp",
                service_name="Gardeners",
            ),
            gap=rx.breakpoints(
                {"0px": "1.5rem", "640px": "2rem"}
            ),
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "640px": "repeat(2, minmax(0, 1fr))",
                    "1024px": "repeat(4, minmax(0, 1fr))",
                }
            ),
        ),
        rx.box(
            create_view_all_services_button(),
            margin_top="3rem",
            text_align="center",
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
        padding_left=rx.breakpoints(
            {
                "0px": "1rem",
                "640px": "1.5rem",
                "1024px": "2rem",
            }
        ),
        padding_right=rx.breakpoints(
            {
                "0px": "1rem",
                "640px": "1.5rem",
                "1024px": "2rem",
            }
        ),
    )


def create_why_choose_us_content():
    """Create the content for the 'Why Choose SkillConnect?' section."""
    return rx.box(
        rx.flex(
            create_colored_icon(
                alt_text="Verified Icon",
                icon_color="#10B981",
                icon_tag="check-circle",
            ),
            create_info_box(
                title="Verified Professionals",
                description="All tradespeople are vetted and background-checked for your peace of mind",
            ),
            display="flex",
            align_items="flex-start",
        ),
        rx.flex(
            create_colored_icon(
                alt_text="Quality Icon",
                icon_color="#F59E0B",
                icon_tag="star",
            ),
            create_info_box(
                title="Quality Assurance",
                description="Detailed reviews and ratings to ensure top-notch service every time",
            ),
            display="flex",
            align_items="flex-start",
        ),
        rx.flex(
            create_colored_icon(
                alt_text="Security Icon",
                icon_color="#3B82F6",
                icon_tag="shield",
            ),
            create_info_box(
                title="Secure Platform",
                description="Safe and secure transactions and communication for your protection",
            ),
            display="flex",
            align_items="flex-start",
        ),
        gap="2rem",
        display="grid",
        grid_template_columns=rx.breakpoints(
            {
                "0px": "repeat(1, minmax(0, 1fr))",
                "768px": "repeat(3, minmax(0, 1fr))",
            }
        ),
    )


def create_why_choose_us_section():
    """Create the complete 'Why Choose SkillConnect?' section."""
    return rx.box(
        rx.box(
            create_centered_heading(
                content="Why Choose SkillConnect?"
            ),
            create_why_choose_us_content(),
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
        id="about-us",
        background_color="#ffffff",
        padding_top="4rem",
        padding_bottom="4rem",
    )


def create_call_to_action_section():
    """Create the call-to-action section with sign-up options."""
    return rx.box(
        rx.heading(
            "Ready to Get Started with SkillConnect?",
            font_weight="600",
            margin_bottom="2rem",
            font_size="1.875rem",
            line_height="2.25rem",
            as_="h2",
        ),
        create_styled_paragraph(
            content="Join our community of skilled professionals and satisfied customers today"
        ),
        rx.flex(
            create_styled_button(
                hover_style={"background-color": "#1D4ED8"},
                bg_color="#2563EB",
                href="#sign-up-pro",
                content="Sign Up as a Professional",
            ),
            create_styled_button(
                hover_style={"background-color": "#047857"},
                bg_color="#059669",
                href="#find-service",
                content="Find a Service Provider",
            ),
            display="flex",
            justify_content="center",
            column_gap="1rem",
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
        text_align="center",
    )


def create_main_content():
    """Create the main content of the page including all sections."""
    return rx.box(
        create_hero_container(),
        rx.box(
            create_how_it_works_section(),
            id="how-it-works",
            background_color="#ffffff",
            padding_top="4rem",
            padding_bottom="4rem",
        ),
        rx.box(
            create_featured_services_section(),
            id="services",
            class_name="bg-gradient-to-r from-blue-600 to-blue-800",
            padding_top="4rem",
            padding_bottom="4rem",
            color="#ffffff",
        ),
        create_why_choose_us_section(),
        rx.box(
            create_call_to_action_section(),
            background_color="#F3F4F6",
            padding_top="4rem",
            padding_bottom="4rem",
        ),
    )


def create_footer_content():
    """Create the content for the footer section."""
    return rx.box(
        rx.box(
            create_styled_heading(
                heading_level="h4",
                font_size="1.125rem",
                margin_bottom="1rem",
                content="SkillConnect",
            ),
            create_colored_text(
                color="#9CA3AF",
                content="Connecting skilled professionals with those who need their services for all home improvement projects.",
            ),
        ),
        rx.box(
            create_styled_heading(
                heading_level="h4",
                font_size="1.125rem",
                margin_bottom="1rem",
                content="Quick Links",
            ),
            rx.list(
                create_list_item_with_anchor(
                    hover_style={"color": "#ffffff"},
                    color="#9CA3AF",
                    href="#",
                    content="Home",
                ),
                create_list_item_with_anchor(
                    hover_style={"color": "#ffffff"},
                    color="#9CA3AF",
                    href="#about-us",
                    content="About Us",
                ),
                create_list_item_with_anchor(
                    hover_style={"color": "#ffffff"},
                    color="#9CA3AF",
                    href="#services",
                    content="Services",
                ),
                create_list_item_with_anchor(
                    hover_style={"color": "#ffffff"},
                    color="#9CA3AF",
                    href="#contact",
                    content="Contact",
                ),
                display="flex",
                flex_direction="column",
                gap="0.5rem",
            ),
        ),
        rx.box(
            create_styled_heading(
                heading_level="h4",
                font_size="1.125rem",
                margin_bottom="1rem",
                content="Legal",
            ),
            rx.list(
                create_list_item_with_anchor(
                    hover_style={"color": "#ffffff"},
                    color="#9CA3AF",
                    href="#terms",
                    content="Terms of Service",
                ),
                create_list_item_with_anchor(
                    hover_style={"color": "#ffffff"},
                    color="#9CA3AF",
                    href="#privacy",
                    content="Privacy Policy",
                ),
                create_list_item_with_anchor(
                    hover_style={"color": "#ffffff"},
                    color="#9CA3AF",
                    href="#cookie",
                    content="Cookie Policy",
                ),
                display="flex",
                flex_direction="column",
                gap="0.5rem",
            ),
        ),
        rx.box(
            create_styled_heading(
                heading_level="h4",
                font_size="1.125rem",
                margin_bottom="1rem",
                content="Follow Us",
            ),
            rx.flex(
                create_social_media_link(
                    href="https://facebook.com/skillconnect",
                    icon_alt="Facebook",
                    icon_tag="facebook",
                ),
                create_social_media_link(
                    href="https://twitter.com/skillconnect",
                    icon_alt="Twitter",
                    icon_tag="twitter",
                ),
                create_social_media_link(
                    href="https://instagram.com/skillconnect",
                    icon_alt="Instagram",
                    icon_tag="instagram",
                ),
                create_social_media_link(
                    href="https://linkedin.com/company/skillconnect",
                    icon_alt="LinkedIn",
                    icon_tag="linkedin",
                ),
                display="flex",
                column_gap="1rem",
            ),
        ),
        gap="2rem",
        display="grid",
        grid_template_columns=rx.breakpoints(
            {
                "0px": "repeat(1, minmax(0, 1fr))",
                "768px": "repeat(4, minmax(0, 1fr))",
            }
        ),
    )


def create_footer():
    """Create the complete footer section with content and copyright."""
    return rx.box(
        create_footer_content(),
        rx.box(
            rx.text(
                "© 2023 SkillConnect. All rights reserved. | Address: 123 Main St, Anytown, USA 12345 | Phone: (555) 123-4567 | Email: info@skillconnect.com"
            ),
            border_color="#374151",
            border_top_width="1px",
            margin_top="2rem",
            padding_top="2rem",
            text_align="center",
            color="#9CA3AF",
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


def create_page_layout():
    """Create the overall page layout including header, main content, and footer."""
    return rx.box(
        rx.box(
            create_responsive_header(),
            background_color="#ffffff",
            box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
        ),
        create_main_content(),
        rx.box(
            create_footer(),
            id="contact",
            background_color="#1F2937",
            padding_top="2rem",
            padding_bottom="2rem",
            color="#ffffff",
        ),
        class_name="font-['Poppins']",
        background_color="#F3F4F6",
    )


def create_page():
    """Create the complete page with all necessary elements and styling."""
    return rx.fragment(
        create_link_element(
            href="https://www.skillconnect.com",
            rel="canonical",
        ),
        # rx.script(src="https://cdn.tailwindcss.com"),
        create_link_element(
            href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap",
            rel="stylesheet",
        ),
        # rx.el.style(
        #     """
        #         @font-face {
        #             font-family: 'LucideIcons';
        #             src: url(https://unpkg.com/lucide-static@latest/font/Lucide.ttf) format('truetype');
        #         }
        #     """
        # ),
        create_page_layout(),
    )