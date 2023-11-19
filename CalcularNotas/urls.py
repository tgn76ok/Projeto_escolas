from django.urls import path

from . import views

app_name = 'Notas'

urlpatterns = [
    path('', views.homeProva, name="homev"),
    # path('Prova/search/', views.search, name="search"),
    # path('Prova/category/<int:category_id>/',
    #      views.category, name="category"),
    
]