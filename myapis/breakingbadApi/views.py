from django.shortcuts import render
import requests
from django.shortcuts import redirect

# Create your views here.
def home (request):
    url = "https://breakingbadapi.com/api/characters"
    data_personajes = requests.get(url)
    data_personajes = data_personajes.json()
    return render(request, "breakingbadApi/home.html", {"personajes":data_personajes})

def episodios (request):
    url = "https://breakingbadapi.com/api/episodes"
    data_episodios = requests.get(url)
    data_episodios = data_episodios.json()
    return render(request, "breakingbadApi/episodios.html", {"episodios":data_episodios})

