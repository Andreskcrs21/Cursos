from django.contrib import admin
from .models import Curso

# Register your models here.
class CursoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'curso_titulo', 
        'curso_contenido',
        'curso_publicado',
        'costo',
        )

    

admin.site.register(Curso, CursoAdmin)