from playwright.async_api import Page

NOMBRE_PORTAL = "fiscal"

async def consultar(page: Page, cedula: str) -> str:
    await page.goto("https://www.fiscalia.gov.co/colombia/")
    # TODO: Implementar scraping real
    return "Resultado de fiscal para " + cedula
