from django.http import HttpResponse
from django.template import Template, Context, loader

from datetime import datetime

def saludo(request):
    return HttpResponse('<h1>Hola Django - Coder! </h1>')

def iniciar_sesion(request):
    return HttpResponse('Pasame tu password y tu username por Whatsapp ;)')


def dia_hoy(request, nombre):
    hoy = datetime.now()
    respuesta = f'Hoy es {hoy} - Bienvenid@ {nombre}'
    return HttpResponse(respuesta)

def nacimiento(request, edad):
    edad = int(edad)
    anio_nac = datetime.now().year - edad
    return HttpResponse(f'Naciste en el {anio_nac}')

def vista_plantilla(request):

    #Abrimos el archivo
    archivo = open(r"C:\Users\MegaTecnologia\Desktop\python\proyecto1\proyecto1\templates\plantilla.html")

    #Creamos el objeto "plantilla"
    plantilla = Template(archivo.read())

    #Cerramos el archivo para liberar recursos 
    archivo.close()

    #Diccionario con datos para la plantilla
    datos = {"nombre": "Esteban", "apellido": "Fradin", "fecha": datetime.now() }

    #Creamos el contexto
    contexto = Context(datos)

    #Renderizamos la plantilla para crear la respuesta 
    documento = plantilla.render(contexto)

    #Retornamos la respuesta 
    return HttpResponse(documento)


def vista_listado_alumnos(request):
    archivo = open(r"C:\Users\MegaTecnologia\Desktop\python\proyecto1\proyecto1\templates\listado_alumnos.html")

    plantilla = Template(archivo.read())

    archivo.close()

    listado_alumnos = ["Esteban", "Leonel", "Clara", "Candela", "Giuliano", "Rocio"]
    datos = {"tecnologia":"Python", "listado_alumnos": listado_alumnos}

    contexto = Context(datos)

    documento = plantilla.render(contexto)

    return HttpResponse(documento)

def vista_listado_alumnos2(request):
    listado_alumnos = ["Esteban", "Leonel", "Clara", "Candela", "Giuliano", "Rocio"]
    datos = {"tecnologia":"Python", "listado_alumnos": listado_alumnos}

    plantilla = loader.get_template("listado_alumnos.html")
    documento = plantilla.render({datos})

    return HttpResponse(documento)

