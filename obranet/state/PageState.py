import reflex as rx
from obranet.api.api import list_db


class PageState(rx.State):
    
    list_info:list

    async def list_tabla(self):
        self.list_info = await list_db()