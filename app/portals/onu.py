from playwright.async_api import Page

NOMBRE_PORTAL = "onu"

async def consultar(page: Page, cedula: str) -> str:
    await page.goto("https://www.un.org/es/")
    # TODO: Implementar scraping real
    return "Resultado de onu para " + cedula
