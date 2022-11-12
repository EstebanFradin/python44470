from django.urls import path
from appnew.views import *

urlpatterns = [
    path('inicio/', Inicio),
    path('estudiantes/', Estudiantes),
    path('profesores/', Profesores),
    path('cursos/', Cursos),
    path('entregables/', Entregables),

]