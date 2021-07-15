from django.contrib import admin
from .models import Curso

# Register your models here.
class CursoAdmin(admin.ModelAdmin):
    

    fieldsets = [
        ("Titulo/fecha", {"fields": ["curso_titulo", "curso_publicado"] }),
        ("Contenido", {"fields": ["curso_contenido"]})
    
    ]

admin.site.register(Curso, CursoAdmin)