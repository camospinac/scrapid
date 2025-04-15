# 📌 scrapid

**scrapid** es una API modular y colaborativa para consultar información pública a través de portales oficiales en Colombia, a partir del número de cédula.  
Está pensada como una plataforma de scraping distribuido, abierta a la comunidad para crecer y mantenerse con múltiples fuentes.

> ⚡️ Construida con [FastAPI](https://fastapi.tiangolo.com/) y [Playwright](https://playwright.dev/) para alto rendimiento en scraping.

---

## 🚀 Características

- Consulta múltiples portales simultáneamente por cédula.
- Arquitectura modular: cada portal es independiente.
- Fácil de extender con nuevos portales.
- API asincrónica rápida con FastAPI.
- Preparado para uso open-source y colaborativo.

---

## 🧪 Estado actual

| Portal     | Estado     |
|------------|------------|
| RUES       | ✅ Implementado |
| Función Pública | ✅ Implementado |

---

## 📦 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/tu_usuario/scrapid.git
cd scrapid

# Crear entorno virtual
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt 

```
---

## 🔧 Uso

Levanta el servidor de desarrollo con:

```bash
    uvicorn app.main:app
```
La API estará disponible en:
📍 http://localhost:8000/docs → Documentación interactiva (Swagger)
📍 http://localhost:8000/redoc → Documentación alternativa

---

---

## 🧪 Ejemplo de consulta (cURL)

```bash
    curl -X POST http://localhost:8000/consultar \
    -H "Content-Type: application/json" \
    -d '{
        "cedulas": ["123456789", "987654321"],
        "portales": ["rues", "funpub"]
    }'
```
Respuesta esperada:

```bash
{
  "resultados": {
    "123456789": {
      "rues": "REGISTRO ACTIVO",
      "funpub": "No se encontraron registros"
    },
    "987654321": {
      "rues": "REGISTRO INACTIVO",
      "funpub": "Funcionario registrado"
    }
  }
}
```
---

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Puedes:
- Sugerir o implementar nuevos portales.
- Reportar errores y bugs.
- Mejorar documentación.
- Optimizar el rendimiento del scraping.

---

---

## 📄 Licencia

Este proyecto está licenciado bajo la Licencia [MIT](https://opensource.org/license/mit).
Puedes usarlo, modificarlo y distribuirlo libremente siempre que mantengas el aviso de copyright.

---

---

## 🧠 Autor

Hecho con 💻 y pasión por Camilo Ospina.
¡Gracias por apoyar proyectos open-source hechos en Latinoamérica! 🇨🇴🚀

---