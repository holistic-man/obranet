from .SupabaseAPI import SupabaseAPI

SUPABASE_API = SupabaseAPI()


async def list_db() -> list:
    return SUPABASE_API.lista()