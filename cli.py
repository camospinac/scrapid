import typer
from pathlib import Path

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

async def consultar_{nombre}(page: Page, cedula: str) -> str:
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
        init_path.write_text("PORTALES_DISPONIBLES = {}\n")

    contenido = init_path.read_text(encoding="utf-8").strip().splitlines()

    import_line = f"from . import {nombre}"
    if import_line not in contenido:
        contenido.insert(0, import_line)

    dict_inicio = next((i for i, line in enumerate(contenido) if line.startswith("PORTALES_DISPONIBLES")), None)
    if dict_inicio is not None:
        imports = [line.split()[-1] for line in contenido if line.startswith("from . import ")]
        dict_lines = ["PORTALES_DISPONIBLES = {"]
        for imp in imports:
            dict_lines.append(f'    "{imp}": {imp}.consultar_{imp},')
        dict_lines.append("}")
        contenido = [line for line in contenido if not line.startswith("PORTALES_DISPONIBLES")]
        contenido.extend(dict_lines)

    init_path.write_text("\n".join(contenido) + "\n", encoding="utf-8")

if __name__ == "__main__":
    app()
