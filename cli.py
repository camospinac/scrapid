import typer
from pathlib import Path
import asyncio
from playwright.async_api import async_playwright
from app.portals import PORTALES_DISPONIBLES

app = typer.Typer()

@app.command()
def crear_portal(
    nombre: str = typer.Option(..., "--nombre", "-n", help="Nombre del nuevo portal"),
    url: str = typer.Option(..., "--url", "-u", help="URL del portal")
):
    """Crea un nuevo archivo de portal con una función base y actualiza el __init__.py."""
    
    portal_path = Path(f"app/portals/{nombre}.py")
    if portal_path.exists():
        typer.echo(f"⚠️ El portal '{nombre}' ya existe.")
        raise typer.Exit()

    contenido = f'''from playwright.async_api import Page

NOMBRE_PORTAL = "{nombre}"

async def consultar(page: Page, cedula: str) -> str:
    await page.goto("{url}")
    # TODO: Implementar scraping real
    return "Resultado de {nombre} para " + cedula
'''
    portal_path.write_text(contenido, encoding="utf-8")
    typer.echo(f"✅ Portal '{nombre}' creado en {portal_path}")

    actualizar_init(nombre)
    typer.echo("🔄 Archivo __init__.py actualizado.")

def actualizar_init(nombre: str):
    init_path = Path("app/portals/__init__.py")
    
    if not init_path.exists():
        init_path.write_text("from pathlib import Path\nimport importlib\nimport pkgutil\n\nPORTALES_DISPONIBLES = {}\n")

    contenido = init_path.read_text(encoding="utf-8").strip().splitlines()
    import_line = f"from . import {nombre}"
    
    if import_line not in contenido:
        contenido.insert(0, import_line)

    init_path.write_text("\n".join(contenido) + "\n", encoding="utf-8")


@app.command()
def listar_portales():
    """Lista todos los portales disponibles."""
    typer.echo("📋 Portales disponibles:")
    for nombre in PORTALES_DISPONIBLES:
        typer.echo(f"✅ {nombre}")


@app.command()
def probar_portal(
    portal: str = typer.Option(..., "--portal", "-p", help="Nombre del portal"),
    cedula: str = typer.Option(..., "--cedula", "-c", help="Cédula para probar")
):
    """Prueba un portal específico con una cédula."""
    if portal not in PORTALES_DISPONIBLES:
        typer.echo(f"❌ Portal '{portal}' no está implementado.")
        raise typer.Exit()

    async def ejecutar():
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            resultado = await PORTALES_DISPONIBLES[portal](page, cedula)
            await browser.close()
            return resultado

    resultado = asyncio.run(ejecutar())
    typer.echo(f"🧪 Resultado para portal '{portal}' con cédula '{cedula}':")
    typer.echo(resultado)


if __name__ == "__main__":
    app()







# import typer
# from pathlib import Path

# app = typer.Typer()

# @app.command()
# def crear_portal(
#     nombre: str = typer.Option(..., "--nombre", "-n", help="Nombre del nuevo portal"),
#     url: str = typer.Option(..., "--url", "-u", help="URL del portal")
# ):
#     """Crea un nuevo archivo de portal con una función base y actualiza el __init__.py."""
    
#     portal_path = Path(f"app/portals/{nombre}.py")
#     if portal_path.exists():
#         typer.echo(f"⚠️ El portal '{nombre}' ya existe.")
#         raise typer.Exit()

#     contenido = f'''from playwright.async_api import Page

# NOMBRE_PORTAL = "{nombre}"

# async def consultar(page: Page, cedula: str) -> str:
#     await page.goto("{url}")
#     # TODO: Implementar scraping real
#     return "Resultado de {nombre} para " + cedula
# '''
#     portal_path.write_text(contenido, encoding="utf-8")
#     typer.echo(f"✅ Portal '{nombre}' creado en {portal_path}")

#     actualizar_init(nombre)
#     typer.echo("🔄 Archivo __init__.py actualizado.")

# def actualizar_init(nombre: str):
#     init_path = Path("app/portals/__init__.py")
    
#     if not init_path.exists():
#         init_path.write_text("from pathlib import Path\nimport importlib\nimport pkgutil\n\nPORTALES_DISPONIBLES = {}\n")

#     contenido = init_path.read_text(encoding="utf-8").strip().splitlines()
#     import_line = f"from . import {nombre}"
    
#     if import_line not in contenido:
#         contenido.insert(0, import_line)

#     init_path.write_text("\n".join(contenido) + "\n", encoding="utf-8")

# if __name__ == "__main__":
#     app()
