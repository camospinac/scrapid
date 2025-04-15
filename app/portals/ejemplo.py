from playwright.async_api import Page

NOMBRE_PORTAL = "ejemplo"

async def consultar(page: Page, cedula: str) -> str:
    return f"Esto es un portal de prueba para {cedula}"