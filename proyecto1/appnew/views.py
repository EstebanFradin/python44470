from django.shortcuts import render
from django.http import HttpResponse
from appnew.models import Curso
# Create your views here.

def Inicio(request):
    return render(request,'appnew/index.html')

def Cursos(request):
    return render(request,'appnew/cursos.html')

def Estudiantes(request):
    return render(request, 'appnew/estudiantes.html')

def Profesores(request):
    return render(request, 'appnew/profesores.html')

def Entregables(request):
    return render(request, 'appnew/entregables.html')


# def listado_cursos(request):
#     cursos = Curso.objects.all()
    
#     cadena_respuesta = "<ul>"
#     for curso in cursos:
#         cadena_respuesta += f"<li>({curso.nombre}, {curso.camada}) </li>"
#     cadena_respuesta = "</ul>" 

#     return HttpResponse(cadena_respuesta) 
