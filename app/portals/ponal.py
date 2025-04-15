from playwright.async_api import Page

NOMBRE_PORTAL = "ponal"

async def consultar(page: Page, cedula: str) -> str:
    await page.goto("https://antecedentes.policia.gov.co:7005/WebJudicial/antecedentes.xhtml")
    # TODO: Implementar scraping real
    return "Resultado de ponal para " + cedula
