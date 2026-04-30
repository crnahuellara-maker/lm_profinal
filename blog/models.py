from django.db import models
from ckeditor.fields import RichTextField

class Page(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=150)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='pages', null=True, blank=True)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo
