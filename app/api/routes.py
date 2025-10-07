from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import time

router = APIRouter()
templates = Jinja2Templates(directory="app/templates/fragments")

# --- Datos de muestra (Hardcoded) ---
# En el futuro, esto vendrá de la base de datos
tv_channels_data = [
    {"name": "América TV", "logo": "/static/logos/america_tv.png", "stream_url": "https://example.com/america_tv"},
    {"name": "ATV", "logo": "/static/logos/atv.png", "stream_url": "https://example.com/atv"},
    {"name": "Panamericana", "logo": "/static/logos/panamericana.png", "stream_url": "https://example.com/panamericana"},
    {"name": "Latina", "logo": "/static/logos/latina.png", "stream_url": "https://example.com/latina"},
]

radio_stations_data = {
    "iquitos": [
        {"name": "La Voz de la Selva", "stream_url": "https://example.com/voz_selva"},
        {"name": "Radio Loreto", "stream_url": "https://example.com/radio_loreto"},
        {"name": "Amazónica de Noticias", "stream_url": "https://example.com/amazonica"},
    ],
    "lima": [
        {"name": "RPP Noticias", "stream_url": "https://example.com/rpp"},
        {"name": "Radio Oxígeno", "stream_url": "https://example.com/oxigeno"},
        {"name": "Studio 92", "stream_url": "https://example.com/studio92"},
    ]
}

@router.get("/tv-channels", response_class=HTMLResponse )
async def get_tv_channels(request: Request):
    """
    Devuelve un fragmento HTML con la lista de canales de TV.
    """
    time.sleep(1) # Simula una carga de red
    return templates.TemplateResponse("tv_channels.html", {"request": request, "channels": tv_channels_data})

@router.get("/radios/{region}", response_class=HTMLResponse)
async def get_radio_stations(request: Request, region: str):
    """
    Devuelve un fragmento HTML con las radios de una región específica.
    """
    time.sleep(1) # Simula una carga de red
    stations = radio_stations_data.get(region.lower(), [])
    return templates.TemplateResponse("radio_stations.html", {"request": request, "stations": stations, "region": region.capitalize()})
