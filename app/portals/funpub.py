from playwright.async_api import Page

NOMBRE_PORTAL = "funpub"
async def consultar_funpub(page: Page, cedula: str) -> str:
    await page.goto("https://www.funcionpublica.gov.co/fdci/consultaCiudadana/index")
    await page.fill("#numeroDocumento", cedula)
    await page.keyboard.press("Enter")
    await page.click("#find")
    try:
        await page.wait_for_selector(".table")
        texto = await page.inner_text(".table")
        if "No se encontraron registros" in texto:
            return texto
        return texto.strip()
    except:
        return "Error al consultar en Función Pública"