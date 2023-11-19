from django.db import models

# Create your models here.

class Redacao(models.Model):
    
    name = models.CharField(max_length=250)
    Introducao =  models.TextField()
    Desenvolvimento = models.TextField()
    Conclusao = models.TextField()
    
    img = models.ImageField(upload_to='Redacoes/%Y/%m/%d')
      
    def __str__(self):
        return self.name