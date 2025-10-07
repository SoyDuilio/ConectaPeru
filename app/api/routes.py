from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import time

router = APIRouter()
templates = Jinja2Templates(directory="app/templates/fragments")

# --- DATOS REALES (SUJETOS A CAMBIOS) ---

tv_channels_data = [
    {
        "name": "Latina",
        "stream_url": "https://www.latina.pe/tvenvivo"
    },
    {
        "name": "Panamericana",
        "stream_url": "https://panamericana.pe/tvenvivo"
    },
    {
        "name": "TVPerú",
        "stream_url": "https://www.tvperu.gob.pe/play"
    },
    {
        "name": "ATV",
        "stream_url": "https://www.atv.pe/envivo-atv/"
    },
]

radio_stations_data = {
    "iquitos": [
        {
            "name": "La Voz de la Selva",
            "stream_url": "https://radio3.virtualtronics.com/proxy/lavozdelaselva?mp=/stream"
        },
        {
            "name": "Radio Loreto",
            "stream_url": "https://streaming.gometri.com/stream/8110/;"
        },
        {
            "name": "Radio La Ribereña",
            "stream_url": "https://stream-160.zeno.fm/n063f2g4q8zuv?zs=lBC2yV4bT6q3g3yARrY0qg"
        },
        {
            "name": "Radio Tigre",
            "stream_url": "https://stream-148.zeno.fm/kpg47s59d2zuv?zs=l_uF_1ZcTqKzX0M73VwzLw"
        },
        {
            "name": "Arpeggio",
            "stream_url": "https://stream-163.zeno.fm/023w4b4gq8zuv?zs=4857V_QyR0-a29yT-Uv2hA"
        }
    ],
    "lima": [
        {
            "name": "RPP Noticias",
            "stream_url": "https://playerservices.streamtheworld.com/api/livestream-redirect/GRPPRPPAAC.aac"
        },
        {
            "name": "Ritmo Romántica",
            "stream_url": "https://playerservices.streamtheworld.com/api/livestream-redirect/GRUPORPPRRAAC.aac"
        },
        {
            "name": "Studio 92",
            "stream_url": "https://playerservices.streamtheworld.com/api/livestream-redirect/GRPPST92AAC.aac"
        },
        {
            "name": "Radio La Zona",
            "stream_url": "https://playerservices.streamtheworld.com/api/livestream-redirect/GRPPLZNAAC.aac"
        },
        {
            "name": "Onda Cero",
            "stream_url": "https://14083.live.streamtheworld.com/CRP_OND.mp3"
        }
    ]
}

@router.get("/tv-channels", response_class=HTMLResponse )
async def get_tv_channels(request: Request):
    time.sleep(0.5) # Simula una carga de red ligera
    return templates.TemplateResponse("tv_channels.html", {"request": request, "channels": tv_channels_data})

@router.get("/radios/{region}", response_class=HTMLResponse)
async def get_radio_stations(request: Request, region: str):
    time.sleep(0.5)
    stations = radio_stations_data.get(region.lower(), [])
    return templates.TemplateResponse("radio_stations.html", {"request": request, "stations": stations, "region": region.capitalize()})
