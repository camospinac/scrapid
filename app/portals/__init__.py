from . import onu
from . import fiscal
from . import ponal
from . import rues
from . import funpub

import importlib
import pkgutil
from pathlib import Path

PORTALES_DISPONIBLES = {}

paquete_path = Path(__file__).parent

for _, nombre_modulo, _ in pkgutil.iter_modules([str(paquete_path)]):
    if nombre_modulo.startswith("_"):
        continue
    try:
        modulo = importlib.import_module(f"app.portals.{nombre_modulo}")
        nombre_portal = getattr(modulo, "NOMBRE_PORTAL", None)
        funcion = getattr(modulo, "consultar", None)
        if nombre_portal and funcion:
            PORTALES_DISPONIBLES[nombre_portal] = funcion
    except Exception as e:
        print(f"Error cargando el portal {nombre_modulo}: {e}")
