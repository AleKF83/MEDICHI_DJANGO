from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .forms import LoginForm, AfiliarseForm

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


"""def login(request):
    return render(
        request,
        "app_principal/login.html",
    )"""
"""def login(request):
    if request.method == "POST":
        # Creo la instancia del formulario con los datos cargados en pantalla
        login_form = LoginForm(request.POST)
        # Valido y proceso los datos.
    else:
        # Creo el formulario vacío con los valores por defecto
        login_form = LoginForm()
    
    return render(request, "app_principal/login.html", {'login_form': login_form})"""

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Aquí puedes procesar los datos del formulario
            numero_afiliado = form.cleaned_data['numero_afiliado']
            contrasena = form.cleaned_data['contrasena']
            # Haz lo que necesites con los datos

            # Luego redirige a la página de inicio o donde desees
            return redirect("inicio-pacientes")
    else:
        form = LoginForm()

    return render(request, "app_principal/login.html", {'form': form})

def afiliarse(request):
    if request.method == 'POST':
        form = AfiliarseForm(request.POST)
        #plan_select = AfiliarseForm(request.POST)
        return redirect("index")
    else:
        form = AfiliarseForm()

    return render(request, "app_principal/afiliarse.html", {'form': form})    

"""
def afiliarse(request):
    return render(
        request,
        "app_principal/afiliarse.html",
    )

"""
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
