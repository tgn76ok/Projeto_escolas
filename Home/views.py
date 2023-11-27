from django.shortcuts import render

# Create your views here.
def Home(request):

    return render(request, 'Home/home.html')

def Dicas(request):

    return render(request, 'Home/Dicas.html')

def Assuntos(request):

    return render(request, 'Home/Assuntos.html')

def cronometro(request):

    return render(request, 'Home/cronometro.html')