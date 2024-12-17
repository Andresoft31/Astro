from django.shortcuts import render
from django.http import JsonResponse
import requests

# Configuración global de la API
API_KEY = "47441353-543c78869585ccdaa1ac11f6b"
BASE_URL_IMAGES = "https://pixabay.com/api/"
BASE_URL_VIDEOS = "https://pixabay.com/api/videos/"

def home(request):
    return render(request, "core/home.html")


def sample(request):
    return render(request, "core/sample.html")

def blog(request):
    return render(request, "core/blog.html")





def astro(request):
    # Parámetro de búsqueda para imágenes
    query = request.GET.get("q", "").strip() 
    url = f"{BASE_URL_IMAGES}?key={API_KEY}&q={query}&image_type=photo"
    
    try:
        # Solicitud a la API
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            images= data.get("hits",[])
            # Renderizar plantilla con las imágenes
            return render(request, "core/astro.html", {"images":  images, "query": query})
        else:
            # Manejo de errores HTTP
            return render(request, "core/astro.html", {"error": "No se pudieron obtener imágenes", "query": query})
    except Exception as e:
        # Manejo de excepciones generales
        return render(request, "core/astro.html", {"error": str(e), "query": query})



def clip(request):
    # Parámetro de búsqueda para videos
    query = request.GET.get("q", "")
    url = f"{BASE_URL_VIDEOS}?key={API_KEY}&q={query}&video_type=all"

    try:
        # Solicitud a la API
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # Renderizar plantilla con los videos
            return render(request, "core/clip.html", {"videos": data.get("hits", []), "query": query})
        else:
            # Manejo de errores HTTP
            return render(request, "core/clip.html", {"error": "No se pudieron obtener videos", "query": query})
    except Exception as e:
        # Manejo de excepciones generales
        return render(request, "core/clip.html", {"error": str(e), "query": query})
