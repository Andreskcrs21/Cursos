from django.urls import path, include
from . import views

app_name='main'

urlpatterns = [
    path('', views.homepage, name='homrepage') , 
    path('curso_form/', views.curso_form, name='curso_form'),
    path('lista_form/', views.lista_form, name= 'lista_form'),
    path('editarCurso/<int:id>/', views.editarCurso, name= 'editarCurso'),
    path('eliminarCurso/<int:id>/', views.eliminarCurso, name= 'eliminarCurso'),
    path('inscritos_curso/<int:id>/', views.inscritosCurso, name="inscritos_curso"),
    
    
]
