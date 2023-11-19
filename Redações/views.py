from .models import Redacao
from django.shortcuts import get_list_or_404, get_object_or_404, render

# Create your views here.
def homeRedacoes(request):
    Redacaos = Redacao.objects.all()


    return render(request, 'redacoes/home.html', context={
        'Redacaos': Redacaos,
    })
