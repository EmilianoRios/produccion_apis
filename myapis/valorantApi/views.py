from django.shortcuts import render
import requests

# Create your views here.

def agents(request):

    URL = "https://valorant-api.com/v1/agents?isPlayableCharacter=true"
    query = requests.get(URL)
    agentsJSON = query.json()
    agents = agentsJSON['data']

    return render(request,'valorantApi/agents.html',{'agents':agents})

def agent(request,uuid=None):
    URL = "https://valorant-api.com/v1/agents/%s"%(uuid)
    query = requests.get(URL)
    agentJSON = query.json()
    agent = agentJSON['data']

    return render(request,'valorantApi/agent.html',{'agent':agent})

def weapons(request):
    
    URL = "https://valorant-api.com/v1/weapons"
    query = requests.get(URL)
    weaponsJSON = query.json()
    weapons = weaponsJSON['data']

    return render(request,'valorantApi/weapons.html',{'weapons':weapons})

def weaponsSkins(request,chromas=None):
    if chromas == 'Chromas':
        URL = "https://valorant-api.com/v1/weapons/skinchromas"
    else:
        URL = "https://valorant-api.com/v1/weapons/skins"

    query = requests.get(URL)
    weaponsSkinsJSON = query.json()
    weaponsSkins = weaponsSkinsJSON['data']

    return render(request,'valorantApi/weaponsSkins.html',{'weaponsSkins':weaponsSkins})

def maps(request):
    URL = "https://valorant-api.com/v1/maps"
    query = requests.get(URL)
    mapsJSON = query.json()
    maps = mapsJSON['data']

    return render(request,'valorantApi/maps.html',{'maps':maps})

def map(request,uuid=None):
    URL = "https://valorant-api.com/v1/maps/%s"%(uuid)
    query = requests.get(URL)
    mapJSON = query.json()
    map = mapJSON['data']

    return render(request,'valorantApi/map.html',{'map':map})