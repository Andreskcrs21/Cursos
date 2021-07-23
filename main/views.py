from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Curso
from inscripciones.models import*
from .form import CursoForm
from django.db.models import Sum

# Create your views here.

def homepage(request):
    return render(request,"main/inicio.html", {"cursos": Curso.objects.all})

def curso_form(request):
    if request.method == 'GET':
        form = CursoForm
        contexto = {
        'form' : form
        }
    else:
        form = CursoForm(request.POST)
        contexto = {
        'form' : form
        }
        if form.is_valid():
            form.save()
            return redirect('main:lista_form')

    return render(request,  "main/agregar.html", contexto)

def lista_form(request):
    return render(request, "main/lista.html", {"cursos":Curso.objects.all})


def editarCurso(request,id):
    curso = Curso.objects.get(id = id)
    if request.method == 'GET':
        form = CursoForm(instance= curso)
        contexto = {
            'form': form
        }
    else:
        form = CursoForm(request.POST, instance= curso)
        contexto = {
            'form' : form
        }
        if form.is_valid():
            form.save()
            return redirect('main:lista_form')
    return render(request, "main/agregar.html", contexto)

def eliminarCurso(request,id):
    curso = Curso.objects.get(id = id)
    curso.delete()
    return redirect('main:lista_form')

def inscritosCurso(request, id):
    cursos = Curso.objects.get(id=id)
    inscritos_curso = Inscripcion.objects.filter(curso = cursos)
    suma_costos = inscritos_curso.aggregate(Sum('costo_total'))
    contexto = {
        'cursos': cursos,
        'inscritos_curso': inscritos_curso, 
        'suma_costos': suma_costos  
    }
    return render(request, 'inscripciones/lista_inscritos.html', contexto)