from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from urllib.request import urlopen
import json

def DigimonApi(request):
    url = "https://digimon-api.vercel.app/api/digimon"
    response = urlopen(url)
    data = json.loads(response.read())
    context = { 'data': data}
    
    return render(request, 'digimonApi/index.html', context)

def searchDigimonAPi(request):
    
    succesDigimon = []

    if request.method == 'POST':
        search = request.POST.get('Search').lower()

        url = "https://digimon-api.vercel.app/api/digimon"
        response = urlopen(url)
        data = json.loads(response.read())
        for d in data:
            if search in d['name'].lower():
                succesDigimon.append(d)
            elif search in d['level'].lower():
                succesDigimon.append(d)

    return render(request,'digimonApi/index.html',{'data':succesDigimon})