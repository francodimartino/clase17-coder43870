from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader





def saludar(request):
    return HttpResponse("Hola mundo!")

def segundaVista(request):
    return HttpResponse("<h1>Che! esto viene simple, no es tan complejo!</h1>")

def saludo_con_nombre(request, nombre):
    documento=f"<h1>Hola {nombre}</h1>"
    return HttpResponse(documento)

def calcula_anio_nacimiento(request, edad):
    anio_actual=datetime.datetime.today().year
    anio_nacimiento=anio_actual-int(edad)
    return HttpResponse(f"Usted nacio en el anio {anio_nacimiento}")


# def probandoHtml(request):
#     #cree contexto, por ahora vacio
#     diccionario={"nombre":"Juan", "apellido":"Perez", "edad":30, "lista_de_notas":[1,9,5,4,7,8,2] }
#     #abri archivo
#     archivo=open(r"H:\CODERHOUSE\43870\clase17\proyecto1\plantillas\template1.html")
#     #lei el contenido del archivo
#     contenido=archivo.read()
#     archivo.close()#cerre el archivo
#     template=Template(contenido)#cree el template, con la clase de django
#     contexto=Context(diccionario)#cree el contexto
#     documento=template.render(contexto)#renderice el template con el contexto, mergee
#     return HttpResponse(documento)

def probandoHtml(request):

    diccionario={"nombre":"Juan", "apellido":"Perez", "edad":30, "lista_de_notas":[1,9,5,4,7,8,2] }
    template=loader.get_template("template1.html")
    documento=template.render(diccionario)
    return HttpResponse(documento)