from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from .api import routes as api_routes

app = FastAPI(
    title="Perú Conectado",
    description="WebApp de medios y utilidades de Perú",
    version="0.1.0"
)

# Montar directorio estático para CSS, JS, imágenes, etc.
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Configurar plantillas Jinja2
templates = Jinja2Templates(directory="app/templates")

# Incluir las rutas de la API
app.include_router(api_routes.router, prefix="/api")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Sirve la página principal de la aplicación.
    """
    return templates.TemplateResponse("index.html", {"request": request})
