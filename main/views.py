from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso

# Create your views here.

def homepage(request):
    return render(request,"main/includes/inicio.html", {"cursos": Curso.objects.all})
