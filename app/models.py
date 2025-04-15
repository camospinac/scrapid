from pydantic import BaseModel
from typing import List, Dict

class ConsultaRequest(BaseModel):
    cedulas: List[str]
    portales: List[str]  # Ej: ["rues", "funpub"]

class ConsultaResponse(BaseModel):
    resultados: Dict[str, Dict[str, str]]  # {cedula: {portal: resultado}}