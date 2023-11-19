from django.db import models

# Create your models here.
 
def pdf_upload_path(instance, filename):
    return f'Media/{instance.created_date.strftime("%Y-%m-%d")}_test_{filename}'
class File(models.Model):
    
    pdf = models.FileField(upload_to='Midia/%Y/%m/%d', blank=True)
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name


class Prova(models.Model):
    name = models.CharField(max_length=250)
    
    files = models.ManyToManyField(File, verbose_name="pdfs")
      
    def __str__(self):
        return self.name