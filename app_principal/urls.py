from django.urls import path
from app_principal import views

urlpatterns = [
    path("", views.index, name="index"),
    path("afiliarse", views.afiliarse, name="afiliarse"),
    path("condiciones-privacidad",
        views.condiciones_privacidad,
        name="condiciones-privacidad",
    ),
    path("contactos", views.contactos, name="contactos"),
    path("login", views.login, name="login"),
    path(
        "inicio-pacientes",
        views.inicio_pacientes,
        name="inicio-pacientes",
    ),  # punto del tp
    path(
        "inicio-medicos",
        views.inicio_medicos,
        name="inicio-medicos",
    ),  # punto del tp
    path("portal-medicos", views.portal_medicos, name="portal-medicos"),  # punto del tp
    path("registrarse-cliente", views.registrarse_cliente, name="registrarse-cliente"),
    path("registrar-doctor", views.registrar_doctor, name="registrar-doctor"),
    path("contactos", views.registrar_doctor, name="contactos"),
]
