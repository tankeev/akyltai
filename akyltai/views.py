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

def metod(request):
    return render(request, 'metod.html') 

def kitepkana(request):
    return render(request, 'kitepkana.html')

def sostav(request):
    return render(request, 'sostav.html')
    
def krujok(request):
    return render(request, 'krujok.html')

def menyu(request):
    return render(request, 'menyu.html')