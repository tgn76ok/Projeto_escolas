from .models import Prova
from django.shortcuts import get_list_or_404, get_object_or_404, render

from django.urls import reverse


# Create your views here.
def homeProva(request):
    prova = Prova.objects.all()

    

    return render(request, 'Prova/home.html', context={
        'provas': prova,
    })

def getprova(request, id):
    Provau = get_object_or_404(Prova, pk=id)
    arquivos = Provau.files.values()
    
    url = reverse('home:Home')
    url = url + 'media/'
    print(url)

    return render(request, 'Prova/Prova-view.html', context={
        'provas': Provau,
        'arquivos':arquivos,
        'url_pdf':url
    })
