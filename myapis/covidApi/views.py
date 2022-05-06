from django.shortcuts import render
import requests
import operator
# Create your views here.
def listaPais(request):
    
    URL = 'https://api.covid19api.com/summary'

    data = requests.get(URL)

    data = data.json() 
    data= sorted(data['Countries'], key=lambda k: k['Country'])

    return render(request,'covid/inicio.html',{'Data':data})
