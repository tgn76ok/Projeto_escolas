from django.shortcuts import render

# Create your views here.
def Home(request):

    return render(request, 'Home/Home.html')

def Dicas(request):

    return render(request, 'Home/Dicas.html')

def Assuntos(request):

    return render(request, 'Home/Assuntos.html')