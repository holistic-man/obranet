import os
import dotenv
import requests
import time
from supabase import create_client, Client

class SupabaseAPI:

    dotenv.load_dotenv()
    

    SUPABASE_URL = os.environ.get("SUPABASE_URL")
    SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
    # supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

    def __init__(self) -> None:
        if self.SUPABASE_URL !=  None and self.SUPABASE_KEY != None:
            self.supabase:Client = create_client(
                self.SUPABASE_URL,self.SUPABASE_KEY
            )

  


    def lista(self) -> list:
        response = self.supabase.table("prueba").select("*").execute()

        list_data = []

        if len(response.data) > 0:
            for list_item in response.data:
                list_data.append(list_item)


        print(list_data)
        
        return list_data
    

    def save_user(self,name, email):
        response = (
            self.supabase.table("prueba")
            .insert({"name": name, "email": email})
            .execute()
        )

        return print(response)