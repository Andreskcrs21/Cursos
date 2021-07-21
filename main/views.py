from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Curso
from .form import CursoForm

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