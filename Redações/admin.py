from django.contrib import admin
from .models import Redacao

# Register your models here.
@admin.register(Redacao)
class RedacaoAdmin(admin.ModelAdmin):
    list_display= ('id','name')
    