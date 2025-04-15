from fastapi import APIRouter
from app.models import ConsultaRequest, ConsultaResponse
from app.core.playwright_runner import consultar_cedulas

router = APIRouter()

@router.post("/consultar", response_model=ConsultaResponse)
async def consultar(request: ConsultaRequest):
    resultados = await consultar_cedulas(request)
    return ConsultaResponse(resultados=resultados)