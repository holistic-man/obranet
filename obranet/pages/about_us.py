import reflex as rx
import obranet.utils as utils
import obranet.styles.styles as styles
from obranet.routes import Route
from obranet.components.navbar import navbar
from obranet.components.footer import footer
from obranet.views.about_us.all import create_main_content
from obranet.views.cta import cta
from obranet.components.developed_by import developed_by

from .no_pago import no_pago


@rx.page(
    route=Route.ABOUT_US.value,   
    title=utils.about_us_title,
    # description=utils.about_us_description,
    # image=utils.preview,
    # meta=utils.about_us_meta
)
def about_us() -> rx.Component:
    return rx.box(
        no_pago()
        # navbar(),
        # create_main_content(),
        # cta(),
        # footer(),
        # developed_by()
    )