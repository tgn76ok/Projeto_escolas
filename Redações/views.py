from .models import Redacao
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.urls import reverse

# Create your views here.
def homeRedacoes(request):
    Redacaos = Redacao.objects.all()
    url = reverse('home:Home')
    url = url + 'media/'
    print(url)

    return render(request, 'redacoes/home.html', context={
        'Redacaos': Redacaos,
        'url_pdf':url
    })
