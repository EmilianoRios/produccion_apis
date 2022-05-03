from django.shortcuts import render

# Create your views here.

def menuApis(request):
    return render(request,'menuApis/home.html')