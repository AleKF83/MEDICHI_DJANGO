from django.shortcuts import render
from django.http import HttpResponse

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


def inicio_pacientes(request, nombre_paciente):  # punto del tp
    return HttpResponse(
        f"""
        <h1>Bienvenido {nombre_paciente}</h1>
        <p>Pagina principal del paciente</p>
        """
    )
