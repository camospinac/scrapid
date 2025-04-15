from playwright.async_api import async_playwright
from app.portals import PORTALES_DISPONIBLES

async def consultar_cedulas(request):
    resultados = {}
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        for cedula in request.cedulas:
            resultados[cedula] = {}
            for portal in request.portales:
                try:
                    if portal in PORTALES_DISPONIBLES:
                        page = await browser.new_page()
                        resultado = await PORTALES_DISPONIBLES[portal](page, cedula)
                        resultados[cedula][portal] = resultado
                        await page.close()
                    else:
                        resultados[cedula][portal] = "Portal no implementado"
                except Exception as e:
                    resultados[cedula][portal] = f"Error: {str(e)}"
        await browser.close()
    return resultados
