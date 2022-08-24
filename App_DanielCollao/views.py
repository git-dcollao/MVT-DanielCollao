from multiprocessing import context
from django.shortcuts import render

from App_DanielCollao.models import Familiares
# Create your views here.

def familiares(request):
    familiares = [
        {
        'nombre': "Victor", 
        'apellido': "Collao",
        'parentesco': "Padre",
        'edad': 64,
        'fecha_nacimiento': '1957-07-27'
        },
        {
        'nombre': "Marianela", 
        'apellido': "Vivanco",
        'parentesco': "Madre",
        'edad': 75,
        'fecha_nacimiento': '1958-10-12'
        },
        {
        'nombre': "Victoria", 
        'apellido': "Collao",
        'parentesco': "Hermana",
        'edad': 43,
        'fecha_nacimiento': '1976-09-27'
        },
        {
        'nombre': "Oscar", 
        'apellido': "Collao",
        'parentesco': "Abuelo",
        'edad': 64,
        'fecha_nacimiento': '1928-10-12'
        },
        {
        'nombre': "Fresia", 
        'apellido': "Valladares",
        'parentesco': "Abuela",
        'edad': 84,
        'fecha_nacimiento': '1929-10-12'
        },
        {
        'nombre': "Fresia", 
        'apellido': "Collao",
        'parentesco': "Tía",
        'edad': 57,
        'fecha_nacimiento': '1969-10-12'
        }
    ]
    
    #Familiares(
    #    nombre= "Victor", 
    #    apellido= "Collao",
    #    parentesco= "Padre",
    #    fecha_nacimiento= '1957-07-27'
    #    )
    #familiares.save()

    contexto = {
        'familiares': familiares
    }
    
    return render(request, 'familiar.html', contexto)