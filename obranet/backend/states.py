import reflex as rx
import asyncio
from typing import List, Optional
from obranet.models import Contact
from obranet.models import Registrado
from obranet.routes import Route
from sqlalchemy import select
from sqlmodel import select, func, or_


class UserListState(rx.State):
    
    form_data: dict = {}                # Diccionario que almacena los datos que se rescatan del formulario para luego guardarlos en la BD
    did_submit: bool = False  
    


class ContactState(rx.State):

    is_submmiting: bool = False                # Para efecto de SPINNER al hacer click en ENVIARy que se vea algo    
    success_contact_message : str = "" 
    error_contact_message : str = ""

    

    # Función para formatear el estado del mensaje de error al cargar la pagina de contacto
    def reset_error_message(self):
        self.error_contact_message = ""

    # Función para formatear el estado del mensaje de exito al cargar la pagina de contacto
    def reset_success_message(self):
        self.success_contact_message = ""

    def save_contact_form(self, form_data: dict):
        self.is_submmiting = True
        yield
        try:
            with rx.session() as session:
                new_contact = Contact(**form_data)
                session.add(new_contact)
                session.commit()
                yield
                self.success_contact_message = "Mensaje enviado correctamente."
                # await asyncio.sleep(2)
        except Exception as e:
            self.error_contact_message = "Ha ocurrido un error. Por favor, inténtalo de nuevo."
        self.is_submmiting = False

