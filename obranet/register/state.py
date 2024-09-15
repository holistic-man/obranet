import reflex as rx
import asyncio
from typing import List

class UserRegistered(rx.Base):

    name: str
    email: str
    phone: str
    service: str
    description: str




class FormState(rx.State):
    form_data: dict = {}
    did_submit: bool = False
    users : List[UserRegistered] = []

    @rx.var
    def thank_you(self):
        name= self.form_data.get("name") or ""
        return f"Gracias {name}".strip() + "!"
    
    def append_user(self, name, email, phone, service, description):
        self.users.append(
            UserRegistered(
                name=name,
                email=email,
                phone=phone,
                service=service,
                description=description
            )
        )

    async def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        user_name = form_data.get("name")
        user_email = form_data.get("email")
        user_phone = form_data.get("phone")
        user_service = form_data.get("service")
        user_description = form_data.get("description")
        if user_name and user_email and user_phone and user_service and user_description:
            self.did_submit = True
            self.append_user(user_name,user_email,user_phone,user_service,user_description)
            yield
            await asyncio.sleep(2)
            self.did_submit = False
            yield