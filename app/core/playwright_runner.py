from playwright.async_api import async_playwright
from app.portals import PORTALES_DISPONIBLES
import asyncio

CONCURRENCY_LIMIT = 5

async def consultar_portal(sem, browser, cedula, portal, resultados):
    async with sem:
        try:
            if portal in PORTALES_DISPONIBLES:
                page = await browser.new_page()
                resultado = await PORTALES_DISPONIBLES[portal](page, cedula)
                await page.close()
                resultados[cedula][portal] = resultado
            else:
                resultados[cedula][portal] = "Portal no implementado"
        except Exception as e:
            resultados[cedula][portal] = f"Error: {str(e)}"


async def consultar_cedulas(request):
    resultados = {cedula: {} for cedula in request.cedulas}
    sem = asyncio.Semaphore(CONCURRENCY_LIMIT)
    tareas = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)

        for cedula in request.cedulas:
            for portal in request.portales:
                tarea = consultar_portal(sem, browser, cedula, portal, resultados)
                tareas.append(asyncio.create_task(tarea))

        await asyncio.gather(*tareas)
        await browser.close()

    return resultados