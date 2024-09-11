import reflex as rx
import obranet.utils as utils
import obranet.styles.styles as styles
from obranet.routes import Route
from obranet.components.navbar import navbar
from obranet.components.footer import footer
from obranet.views.header import header
from obranet.views.how_it_works import how_it_works
from obranet.views.featured_services import feature_services
from obranet.views.why_choose_us import why_choose_us
from obranet.views.cta import cta

@rx.page(
    route=Route.INDEX.value,   
    title=utils.index_title,
    # description=utils.index_description,
    # image=utils.preview,
    # meta=utils.index_meta
)
def index() -> rx.Component:
    return rx.box(
        navbar(),
        header(),
        how_it_works(),
        feature_services(),
        why_choose_us(),
        cta(),
        footer(),
        # navbar(),
        # create_hero_container(),
        # create_how_it_works_section(),
        # create_featured_services_section(),
        # create_page()
    )