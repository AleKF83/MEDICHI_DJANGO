from django.urls import path,re_path
from app_principal import views

urlpatterns = [
    path("", views.index, name="index"),
    path("afiliarse", views.afiliarse, name="afiliarse"),
    path("condiciones-privacidad", views.condiciones_privacidad, name="condiciones-privacidad"),
    path("contactos", views.contactos, name="contactos"),
    path("login", views.login, name="login"),
    path("inicio-pacientes", views.inicio_pacientes, name="inicio-pacientes"),
    path("inicio-medicos",views.inicio_medicos, name="inicio-medicos"),
    path("portal-medicos", views.portal_medicos, name="portal-medicos"),
    path("alta-paciente", views.alta_paciente, name="alta-paciente"),
   #path('listado-pacientes', views.listado_pacientes, name='listado_pacientes'),
   # path('alta-profesional', views.alta_profesional, name="alta-profesional"),
    #path('profesionales/listado', views.profesionales_listado, name='profesionales_listado'),
    path("registrarse-cliente", views.registrarse_cliente, name="registrarse-cliente"),
    path("registrar-doctor", views.registrar_doctor, name="registrar-doctor"),
    path("contactos", views.registrar_doctor, name="contactos"),
    re_path(r'pacientes/historico/(?P<year>[0-9]{4})/$', views.pacientes_historico, name='pacientes_historico'),
]
