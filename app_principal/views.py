from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from datetime import datetime, timedelta, date
from .forms import CrearTurnoForm, AfiliarseForm, LoginMedico, AltaAfiliado, EspecialidadForm
from .models import Afiliado, Profesional,Plan, Especialidades, CrearTurno
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
'''
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

'''
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

def inicio_administracion(request):  # punto del tp
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
    return render(request, "app_principal/inicio-administracion.html", context)

def pacientes_historico(request,year):
    return HttpResponse(f'<h1>Historico de Pacientes del año: {year}</h1>')

def alta_afiliado(request):
    context = {}

    if request.method == "POST":
        alta_afiliado_form = AltaAfiliado(request.POST)

        if alta_afiliado_form.is_valid():         
            nombre = alta_afiliado_form.cleaned_data['nombre']
            apellido = alta_afiliado_form.cleaned_data['apellido']
            email = alta_afiliado_form.cleaned_data['email']
            dni = alta_afiliado_form.cleaned_data['dni']
            numeroAfiliado = alta_afiliado_form.cleaned_data['numeroAfiliado']
            plan_pk = alta_afiliado_form.cleaned_data['plan']

            try:                
                plan = Plan.objects.get(pk=plan_pk)
                nuevo_afiliado = Afiliado(
                    nombre=nombre,
                    apellido=apellido,
                    email=email,
                    dni=dni,
                    numeroAfiliado=numeroAfiliado,
                    plan=plan,
                )
                nuevo_afiliado.save()

                messages.info(request, "Afiliado dado de alta correctamente")
                return redirect(reverse("alta-afiliado"))

            except Plan.DoesNotExist:
                messages.error(request, "El Plan seleccionado no es válido.")
            except IntegrityError as ie:
                messages.error(request, "Ocurrió un error al intentar dar de alta al paciente")
                return redirect(reverse("index"))

    else:
        alta_afiliado_form = AltaAfiliado()

    context['alta_afiliado_form'] = alta_afiliado_form
    return render(request, 'app_principal/alta-afiliado.html', context)


def listado_afiliados(request):
    listado = Afiliado.objects.all().order_by('dni')
    context = {

        'listado_afiliados': listado,
        'cant_afiliados': len(listado),
    }

    return render(request, 'app_principal/listado-afiliados.html', context)

class ProfesionalCreateView(CreateView):
    model = Profesional
    template_name = 'app_principal/alta-profesional.html'
    success_url = 'listado-profesionales'
    fields = '__all__'
    
 
class ProfesionalListView(ListView):
    model = Profesional
    context_object_name = 'listado_profesionales'
    template_name = 'app_principal/listado-profesionales.html'
    ordering = ['cuit']
    

def alta_especialidad(request):
    if request.method == 'POST':
        form = EspecialidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado_especialidades')  
    else:
        form = EspecialidadForm()
    return render(request, 'app_principal/alta-especialidad.html', {'form': form})



def modificar_especialidad(request, especialidad_id):
    especialidad = Especialidades.objects.get(pk=especialidad_id)
    if request.method == 'POST':
        form = EspecialidadForm(request.POST, instance=especialidad)
        if form.is_valid():
            form.save()
            return redirect('listado_especialidades')  
    else:  
        form = EspecialidadForm(instance=especialidad)
    
    return render(request, 'app_principal/modificar-especialidad.html', {'form': form})

       

def eliminar_especialidad(request, especialidad_id):
    especialidad = Especialidades.objects.get(pk=especialidad_id)
    especialidad.delete()
    return redirect('listado_especialidades')  

def listado_especialidades(request):
    listado = Especialidades.objects.all()
    context = {

        'listado_especialidades': listado,
        'cant_especialidades': len(listado),
    }

    return render(request, 'app_principal/listado-especialidades.html', context)

def listado_turnos(request):
    # Obtener las listas de especialidades y profesionales
    especialidades = Especialidades.objects.all()
    profesionales = Profesional.objects.all()

    # Obtener los filtros seleccionados por el usuario
    especialidad_id = request.GET.get('especialidad')
    profesional_id = request.GET.get('profesional')
    fecha = request.GET.get('fecha')

    # Filtrar los turnos según los filtros seleccionados
    turnos = CrearTurno.objects.all()

    if especialidad_id:
        turnos = turnos.filter(especialidades__id=especialidad_id)

    if profesional_id:
        turnos = turnos.filter(profesional_id=profesional_id)

    if fecha:
        turnos = turnos.filter(fecha=fecha)

    return render(request, 'app_principal/listado-turnos.html', {'turnos': turnos, 'especialidades': especialidades, 'profesionales': profesionales})


def seleccionar_turno_afiliado(request):
    if request.method == 'POST':
        form = CrearTurnoForm(request.POST)
        if form.is_valid():
            turno = form.cleaned_data['turno']
            afiliado = form.cleaned_data['afiliado']

            if turno.disponible:
                turno.afiliado = afiliado
                turno.disponible = False
                turno.save()
                return redirect('listado_turnos')
            else:
                messages.error(request, 'El turno ya ha sido asignado.')
    else:
        form = CrearTurnoForm()

    return render(request, 'app_principal/seleccionar-turno.html', {'form': form})


#03-11
def registrar_turno_medico(request):
    if request.method == 'POST':
        form = CrearTurnoForm(request.POST)
        if form.is_valid():
            fecha = form.cleaned_data['fecha']
            hora = form.cleaned_data['hora']
            profesional = form.cleaned_data['profesional']

            # Obtener las especialidades del profesional
            especialidades = profesional.especialidades.all()

            # Calcular el rango de tiempo (5 horas)
            hora_fin = datetime.combine(fecha, hora) + timedelta(hours=5)

            # Crear los turnos cada 20 minutos
            intervalo = timedelta(minutes=20)
            hora_actual = datetime.combine(fecha, hora)
            while hora_actual < hora_fin:
                nuevo_turno = CrearTurno(
                    fecha=hora_actual.date(),
                    hora=hora_actual.time(),
                    profesional=profesional,
                    disponible=True  # Asegúrate de marcar el turno como disponible
                )
                nuevo_turno.save()
                nuevo_turno.especialidades.set(especialidades)  # Asignar especialidades

                hora_actual += intervalo

            # Mostrar mensaje de éxito
            messages.success(request, 'Los turnos se han creado correctamente.')
            return redirect('listado_turnos')
    else:
        form = CrearTurnoForm()

    return render(request, 'app_principal/registrar-turno.html', {'form': form})


#06/11
from django.views.generic.edit import UpdateView



class CrearTurnoUpdateView(UpdateView):
    model = CrearTurno
    fields = '__all__'
    #fields = ["Afiliado"]
    template_name_suffix = "_update_form"