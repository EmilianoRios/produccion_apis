from django.shortcuts import render
import requests
from django.shortcuts import redirect


def home (request):
    url="https://api.disneyapi.dev/characters"
    personajes=requests.get(url)
    personajes=personajes.json()
    data=personajes["data"]

    for i in data:
        if i["films"] == [] or i["enemies"] == [] or i["videoGames"] == []:
            i["films"] = "No hay peliculas"
            i["enemies"] = "No hay enemigos"
            i["videoGames"] = "No hay juegos"

    return render(request, "disneyApi/disney.html", {"personajes":data})


