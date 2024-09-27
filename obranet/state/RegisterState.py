import reflex as rx
import asyncio
from typing import List, Optional
from obranet.models import Registrado
from obranet.routes import Route
from sqlalchemy import select
from sqlmodel import select, func, or_


class RegisterState(rx.State):
    
    form_data: dict = {}                # Diccionario que almacena los datos que se rescatan del formulario para luego guardarlos en la BD
    did_submit: bool = False            # Si el usuario hace click en registrar o no
    
    users : List['Registrado'] = []     # Diccionado que almacena todos los registros de la tabla Registrado
    user: Optional['Registrado'] = None
    total_users: int = 0                # Contador del total de usuarios
    offset: int = 0                     # Para paginación (parte en 0 y se muestran 10)
    limit: int = 9                      # Para paginación
    is_loaded: bool = False             # Para mostrar SKELETON cuando está cargando la consulta
    is_loading:bool = False             # Skeleton para perfil dedicado

    # Nuevas variables para el filtro
    service_filter: str = ""
    location_filter: str = ""
    search_filter: str = ""
    is_applying_filters: bool = False       # Estado de carga para aplicar Spinner a Aplicar Filtro
    is_clearing_filters: bool = False       # Estado de carga para aplicar Spinner a Limpiar Filtro
    is_submmiting: bool = False                # Para efecto de SPINNER al hacer click en REGISTRAR botón y que se vea algo
    

    error_registration_message: str = ""    #Resetea el mensaje de error para que no aparezca al entrar nuevamente a la pagina de registro
    success_registration_message: str = ""  # Lo mismo pero con el mensaje de exito
    should_reset: bool = False              # NO FUNCIONA

    @rx.var
    def thank_you(self):
        name= self.form_data.get("name") or ""
        return f"Gracias {name}".strip() + "!"
    
    # Variable para calcular el número de página actual
    @rx.var(cache=True)
    def page_number(self) -> int:
        return (
            (self.offset // self.limit)
            + 1
            + (1 if self.offset % self.limit else 0)
        )

    # Variable para calcular el número de páginas que debe desplegar
    @rx.var(cache=True)
    def total_pages(self) -> int:
        return self.total_users // self.limit + (
            1 if self.total_users % self.limit else 0
        )
    
    # Variable para deshabilitar el botón ANTERIOR si es la primera página
    @rx.var
    def is_first_page(self) -> bool:
        return self.offset == 0

    # Variable para deshabilitar el botón SIGUIENTE si es la última página
    @rx.var
    def is_last_page(self) -> bool:
        return self.offset + self.limit >= self.total_users
    
    @rx.var
    def filtered_users(self) -> list[Registrado]:
        users = self.users

        if self.service_filter:
            users = [user for user in users if user.service == self.service_filter]

        if self.location_filter:
            users = [user for user in users if user.location == self.location_filter]

        if self.search_filter:
            users = [user for user in users if self.search_filter.lower() in user.name.lower() or self.search_filter.lower() in user.service.lower() or self.search_filter.lower() in user.description.lower()]

        return users

    @rx.var
    def user_id(self):
        return self.router.page.params.get("user_id","")
    
    @rx.var
    def service(self) -> str:
        return self.router.page.params.get("service", "")

    @rx.var
    def name(self) -> str:
        return self.router.page.params.get("name", "")

    def apply_filters(self):
        self.is_applying_filters = True
        yield
        self.page_number = 1
        self.offset = 0
        self.load_entries()
        self.is_applying_filters = False

    def clear_filters(self):
        self.is_clearing_filters = True
        yield
        self.service_filter = ""
        self.location_filter = ""
        self.search_filter = ""
        self.page_number = 1
        self.offset = 0
        self.load_entries()
        self.is_clearing_filters = False

    # Función para cambiar a la pagina anterior
    def prev_page(self):
        self.offset = max(self.offset - self.limit, 0)
        self.load_entries()

    # Función para cambiar a la pagina siguiente
    def next_page(self):
        if self.offset + self.limit < self.total_users:
            self.offset += self.limit
        self.load_entries()

    def _get_total_users(self, session):
        query = select(func.count(Registrado.id))
        # Aplicar los mismos filtros a la consulta de conteo
        if self.service_filter and self.service_filter != "all":
            query = query.where(Registrado.service == self.service_filter)
        if self.location_filter and self.location_filter != "all_location":
            query = query.where(Registrado.location == self.location_filter)
        if self.search_filter:
            search_value = f"%{self.search_filter.lower()}%"
            query = query.where(
                or_(
                    Registrado.name.ilike(search_value),
                    Registrado.service.ilike(search_value),
                    Registrado.description.ilike(search_value)
                )
            )
        
        self.total_users = session.exec(query).one()

    # Función para obtener el total de usuarios en la BD
    def load_entries(self) -> list[Registrado]:
        self.is_loaded = False
        with rx.session() as session:
            query = select(Registrado)

            # Aplicar filtros a la consulta
            if self.service_filter and self.service_filter != "all":
                query = query.where(Registrado.service == self.service_filter)
            if self.location_filter and self.location_filter != "all_location":
                query = query.where(Registrado.location == self.location_filter)
            if self.search_filter:
                search_value = f"%{self.search_filter.lower()}%"
                query = query.where(
                    or_(
                        Registrado.name.ilike(search_value),
                        Registrado.service.ilike(search_value),
                        Registrado.description.ilike(search_value)
                    )
                )
            # Apply pagination
            query = query.offset(self.offset).limit(self.limit)
            self.users = session.exec(query).all()
            self._get_total_users(session)
        self.is_loaded = True

    def get_user_detail(self):
        self.is_loaded = False
        self.user = None  # Resetea el usuario para evitar mostrar datos anteriores
        yield
        with rx.session() as session:
            result = session.exec(
                Registrado.select().where(
                    (Registrado.service == self.service) & 
                    (Registrado.name == self.name)
                )
            ).one_or_none()
            self.user = result
        self.is_loaded = True

    # Función para formatear el estado del mensaje de error al cargar la pagina de registro
    def reset_error_message(self):
        self.error_registration_message = ""

    # Función para formatear el estado del mensaje de exito al cargar la pagina de registro
    def reset_success_message(self):
        self.success_registration_message = ""

    # Función para formatear el estado de la paginación al cargar la pagina de servicios
    def reset_pagination(self):
        self.offset = 0
        self.load_entries()
    
    # Función para añadir los datos de un usuario a la BD
    def append_user(self, name, email, phone, location, service, description):
        with rx.session() as session:
            obj = Registrado(
                    name=name,
                    email=email,
                    phone=phone,
                    location=location,
                    service=service,
                    description=description
                )
            session.add(obj)
            session.commit()

    # Funcion asincrona para rescatar los datos del formulario de registro e intentar insertarlos en la BD con la funcion APPEND_USER()
    async def handle_submit(self, form_data: dict):
        self.is_submmiting = True
        yield
        try:
            """Handle the form submit."""
            self.form_data = form_data
            user_name = form_data.get("name")
            user_email = form_data.get("email")
            user_phone = form_data.get("phone")
            user_location = form_data.get("location")
            user_service = form_data.get("service")
            user_description = form_data.get("description")
            if user_name and user_email and user_phone and user_location and user_service and user_description:
                self.append_user(user_name,user_email,user_phone,user_location,user_service,user_description)
                yield
                await asyncio.sleep(2)
                # self.did_submit = False
                self.is_submmiting = False
                self.success_registration_message = "Te registraste correctamente."
                self.did_submit = True
                yield rx.redirect(Route.INDEX.value)

        except Exception as e:
            if "UniqueViolation" in str(e):
                self.error_registration_message = "El correo que estás utilizando ya se encuentra registrado en nuestra base de datos. Intenta con otro."
            else:
                self.error_registration_message = "Ha ocurrido un error. Por favor, inténtalo de nuevo."
        self.is_submmiting = False





