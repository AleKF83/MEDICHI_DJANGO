from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from datetime import datetime
from .forms import LoginPaciente, AfiliarseForm, LoginMedico, AltaAfiliado, AltaProfesionalModelForm
from .models import Afiliado, Profesional
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.db import IntegrityError
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
    if request.method == 'POST':
        form = LoginPaciente(request.POST)
        if form.is_valid():
            # Para procesar los datos del formulario
            #numero_afiliado = form.cleaned_data['numero_afiliado']
            #contrasena = form.cleaned_data['contrasena']
            
            # Si es valido, va al portal
            return redirect(reverse ("inicio-pacientes"))
    else:
        form = LoginPaciente()

    return render(request, "app_principal/login.html", {'form': form})

def portal_medicos(request):
    if request.method == 'POST':
        form = LoginMedico(request.POST)
        if form.is_valid():
            # Aquí puedes procesar los datos del formulario
            matricula = form.cleaned_data['matricula']
            contrasena = form.cleaned_data['contrasena']
            # Haz lo que necesites con los datos

            # Luego redirige a la página de inicio o donde desees
            return redirect(reverse ("inicio-medicos"))
    else:
        form = LoginMedico()

    return render(request, "app_principal/portal-medicos.html", {'form': form})

def afiliarse(request):
    if request.method == 'POST':
        afiliarse = AfiliarseForm(request.POST)
        
        if afiliarse.is_valid():

            messages.success(request, 'Datos enviados con éxito.')
            
            return redirect(reverse("index"))
    else:
        afiliarse = AfiliarseForm()
    
    context = {
        'afiliarse_form': afiliarse
    }

    return render(request, "app_principal/afiliarse.html", context)

def condiciones_privacidad(request):
    return render(
        request,
        "app_principal/condiciones-privacidad.html",
    )
  


def registrarse_cliente(request):
    
    #formulario_registro_cliente = 
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
    "Lucas Romualdo",
    "Betiana Quiroga",


    ]

    context = {
        "nombre_usuario": "griselda lopez",
        "fecha": datetime.now(),
        "genero": 'Femenino',
        "listado_doctores": listado,
        "cant_pacientes": len(listado),
    }

    return render(request, "app_principal/inicio-pacientes.html", context)


def inicio_medicos(request):  # punto del tp
    # Esta data en el futuro vendrá de la base de datos
    listado = [
    "Lucas Romualdo",
    "Betiana Quiroga",

   
        
    ]

    context = {
        "nombre_doctor": "gonzalo cardozo",
        "fecha": datetime.now(),
        "genero": 'Masculino',
        "listado_pacientes": listado,
        "cant_pacientes": len(listado),
    }

    return render(request, "app_principal/inicio-medicos.html", context)

def pacientes_historico(request,year):
    return HttpResponse(f'<h1>Historico de Pacientes del año: {year}</h1>')

def alta_afiliado(request):
    context = {}

    if request.method == "POST":
        alta_afiliado = AltaAfiliado(request.POST)

        if alta_afiliado.is_valid():
            nuevo_afiliado= Afiliado(
                nombre = alta_afiliado.cleaned_data['nombre'],
                apellido = alta_afiliado.cleaned_data['apellido'],
                email = alta_afiliado.cleaned_data['email'],
                dni = alta_afiliado.cleaned_data['dni'],
                numeroAfiliado = alta_afiliado.cleaned_data['numeroAfiliado'],
            )

            try:
                nuevo_afiliado.save()

            except IntegrityError as ie:
                messages.error(request, "Ocurrió un error al intentar dar de alta al paciente")
                return redirect(reverse("index"))

            messages.info(request, "Afiliado dado de alta correctamente")
            return redirect(reverse("listado_pacientes"))
    else:
        alta_afiliado = AltaAfiliado()

    context['alta_afiliado_form'] = AltaAfiliado
    return render(request, 'app_principal/alta-afiliado.html', context)

def listado_pacientes(request):
    listado = Afiliado.objects.all().order_by('dni')
    context = {
        'nombre_usuario': 'Carlos Perez',
        'fecha': datetime.now(),
        'es_instructor': False,
        'listado_alumnos': listado,
        'cant_inscriptos': len(listado),
    }

    return render(request, 'core/alumnos_listado.html', context)