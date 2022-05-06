from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    if request.GET.get('title'):
        URL = 'https://inshortsapi.vercel.app/news?category=all'
        data = requests.get(URL)
        data = data.json() 
        for dic in data['data']:
            if request.GET.get('title')==dic['title']:
                print(dic)
                return render(request, 'noticia/noticias.html', {'data':dic})
    URL = 'https://inshortsapi.vercel.app/news?category=all'
    data = requests.get(URL)
    data = data.json() 
    data['categorias']={'all':'Todos', 'national':'Nacional', 'business':'Negocios', 'sports':'Deportes', 'world':'Mundo', 'politics':'Politica','technology':'Tecnologia', 'entertainment':'Entretenimiento', 'science':'Ciencia', 'automobile':'Automoviles'}
    return render(request, 'noticias/noticias.html', {'data':data})

def filtro(request, categoria):

    URL= 'https://inshortsapi.vercel.app/news?category='+categoria
    data=requests.get(URL)
    data= data.json()
    data['categorias']={'all':'Todos', 'national':'Nacional', 'business':'Negocios', 'sports':'Deportes', 'world':'Mundo', 'politics':'Politica','technology':'Tecnologia', 'entertainment':'Entretenimiento', 'science':'Ciencia', 'automobile':'Automoviles'}
    
    return render(request, 'noticias/filtro.html', {'data':data})

def noticia(request, title):
    URL = 'https://inshortsapi.vercel.app/news?category=all'
    data = requests.get(URL)
    data = data.json() 
    for dic in data['data']:
        if title==dic['title']:
            return render(request, 'noticias/noticia.html', {'data':dic})

    else:
        return render(request, 'noticias/noticias.html', {'data':data})
