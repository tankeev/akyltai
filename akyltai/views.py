from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def info(request):
    return render(request, 'info.html')

def kabyl_aluu(request):
    return render(request, 'kabyl_aluu.html')
    
def daty(request):
    return render(request, 'daty.html')
    
def obrazovanie(request):
    return render(request, 'obrazovanie.html')

def rasp(request):
    return render(request, 'rasp.html')