from django.shortcuts import render
import requests

def formu(request):
     
    return render(request,'horoscopoApi/formu.html')

def horoscopoApi(request):

    signo=request.GET["signos"]
    dia=request.GET["dia"]

    params = (('sign', signo),('day', dia),)
    
    info=requests.post('https://aztro.sameerkumar.website/', params=params)
    
    imagen = "horoscopoApi/img/%s.png"%(signo)
            
    return render(request,'horoscopoApi/horoscopoApi.html',{"json":info.json(),"sign":signo,"imagen":imagen})