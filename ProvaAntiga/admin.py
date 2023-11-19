from django.contrib import admin
from .models import File,Prova
# Register your models here.


@admin.register(Prova)
class ProvaAdmin(admin.ModelAdmin):
    list_display= ('id','name')
    
@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display= ('id',)