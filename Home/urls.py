from django.urls import include, path
from .views import Home,Dicas,Assuntos
from ProvaAntiga.views import homeProva
from CalcularNotas.views import homeNotas
from Redações.views import homeRedacoes
from authors import views

app_name = 'home'

urlpatterns = [
    path('', Home,name="Home"),
    path('Prova/', homeProva,name='prova'),
    path('Notas/', homeNotas,name='notas'),
    path('Dicas/', Dicas,name='Dicas'),
    path('Assuntos/', Assuntos,name='Assuntos'),
    path('Redacoes/', homeRedacoes,name='Redacoes'),
    path('login/', views.login_view, name='login'),
    
]