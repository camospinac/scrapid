from playwright.async_api import Page

NOMBRE_PORTAL = "rues"

async def consultar(page: Page, cedula: str) -> str:
    await page.goto("https://www.rues.org.co/RM/Consultas")
    await page.fill("#search", cedula)
    await page.keyboard.press("Enter")
    await page.wait_for_selector('div.registroapi span')
    estado = await page.inner_text('div.registroapi span')
    return f"REGISTRO {estado.upper()}"