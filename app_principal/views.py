from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.


def index(request):
    return render(
        request,
        "app_principal/index.html",
    )


def contactos(request):
    return render(
        request,
        "app_principal/contactos.html",
    )


def login(request):
    return render(
        request,
        "app_principal/login.html",
    )


def afiliarse(request):
    return render(
        request,
        "app_principal/afiliarse.html",
    )


def condiciones_privacidad(request):
    return render(
        request,
        "app_principal/condiciones-privacidad.html",
    )


def portal_medicos(request):
    return render(
        request,
        "app_principal/portal-medicos.html",
    )


def registrarse_cliente(request):
    return render(
        request,
        "app_principal/registrarse-cliente.html",
    )


def registrar_doctor(request):
    return render(
        request,
        "app_principal/registrar-doctor.html",
    )


def inicio_pacientes(request):  # punto del tp
    # Esta data en el futuro vendrá de la base de datos
    listado = [
        "Carlos Lopez",
        "Maria Del Cerro",
    ]

    context = {
        "nombre_usuario": "Carlos Perez",
        "fecha": datetime.now(),
        "es_instructor": False,
        "listado_alumnos": listado,
        "cant_inscriptos": len(listado),
    }

    return render(request, "app_principal/inicio-pacientes.html", context)


def inicio_medicos(request):  # punto del tp
    # Esta data en el futuro vendrá de la base de datos
    listado = [
        "Sergio Diaz",
        "Susana Medina",
        "Arsenio Mera",
        "Patricia Acosta",
        "Mauricio Ruiz",
        "Jorge Acosta",
        
        
    ]

    context = {
        "nombre_doctor": "gonzalo cardozo",
        "fecha": datetime.now(),
        "genero": 'Masculino',
        "listado_pacientes": listado,
        "cant_pacientes": len(listado),
    }

    return render(request, "app_principal/inicio-medicos.html", context)
