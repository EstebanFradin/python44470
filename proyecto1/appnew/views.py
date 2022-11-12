from django.shortcuts import render
from django.http import HttpResponse
from appnew.models import Curso
# Create your views here.

def Inicio(request):
    return render(request,'appnew/index.html')

def Cursos(request):
    return HttpResponse('Estas en el apartado de cursos')

def Estudiantes(request):
    return HttpResponse('Estas en el apartado de estudiantes')

def Profesores(request):
    return HttpResponse('Estas en el apartado de profesores')

def Entregables(request):
    return HttpResponse('Estas en el apartado de entregables')


# def listado_cursos(request):
#     cursos = Curso.objects.all()
    
#     cadena_respuesta = "<ul>"
#     for curso in cursos:
#         cadena_respuesta += f"<li>({curso.nombre}, {curso.camada}) </li>"
#     cadena_respuesta = "</ul>" 

#     return HttpResponse(cadena_respuesta) 
