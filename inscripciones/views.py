from main.models import Curso
from sys import prefix
from typing import ContextManager
from django.shortcuts import render, redirect
from .models import Inscripcion
from .form import InscripcionForm, RegistroForm

# Create your views here.

def inscripcionesform(request,pk):
    
    registro_form = RegistroForm(prefix='form_registro')
    inscripcion_form = InscripcionForm(prefix='form inscripcion') 

    contexto = {
        'registro_form':registro_form,
        'inscripcion_form':inscripcion_form

    }
    if request.method == 'POST':
        registro_form = RegistroForm(request.POST, prefix='form_registro')
        inscripcion_form = InscripcionForm(request.POST, prefix='form inscripcion')
        
        if registro_form.is_valid() and inscripcion_form.is_valid():
            estudiante = registro_form.save(commit=False)
            estudiante.user = request.user
            estudiante.save()
            curso = Curso.objects.get(pk = pk)
            inscripcion = inscripcion_form.save(commit=False)
            inscripcion.curso = curso
            inscripcion.estudiante = estudiante
            inscripcion.save()
            return redirect('main/lista_estudiantes')
            
    return render(request,'inscripciones/estudiantes.html', contexto)

def lista_estudiantes(request):
    return render(request, "inscripciones/lista.html", {"inscripcion":Inscripcion.objects.all})
