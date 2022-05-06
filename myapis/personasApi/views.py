from django.shortcuts import render
import requests

def personasApi(request):
    
    info=requests.get('https://randomuser.me/api/')
    
    info = info.json()
    
    info = info['results']
    
    info = info[0]
    
    info2=requests.get('https://randomuser.me/api/')
     
    info2 = info2.json()
    
    info2 = info2['results']
    
    info2 = info2[0]
    
    return render(request,'personasApi/personasApi.html',{"persona":info,"persona2":info2},)