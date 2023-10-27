from django.urls import path,re_path
from app_principal import views

urlpatterns = [
    path("", views.index, name="index"),
    path("afiliarse", views.afiliarse, name="afiliarse"),
    path("condiciones-privacidad", views.condiciones_privacidad, name="condiciones-privacidad"),
    path("contactos", views.contactos, name="contactos"),
    path("login", views.login, name="login"),
    path("inicio-administracion", views.inicio_administracion, name="inicio-administracion"),
    path("inicio-pacientes", views.inicio_pacientes, name="inicio-pacientes"),
    path("inicio-medicos",views.inicio_medicos, name="inicio-medicos"),
    path("portal-medicos", views.portal_medicos, name="portal-medicos"),
    path("alta-afiliado", views.alta_afiliado, name="alta-afiliado"),
    path("alta-especialidad", views.alta_especialidad, name="alta-especialidad"),
    path('listado-especialidades', views.listado_especialidades, name='listado_especialidades'),
    path('listado-afiliados', views.listado_afiliados, name='listado_afiliados'),
    path("registrarse-cliente", views.registrarse_cliente, name="registrarse-cliente"),
    path("registrar-doctor", views.registrar_doctor, name="registrar-doctor"),
    path("contactos", views.registrar_doctor, name="contactos"),
    re_path(r'pacientes/historico/(?P<year>[0-9]{4})/$', views.pacientes_historico, name='pacientes_historico'),
    
    path('alta-profesional', views.ProfesionalCreateView.as_view(), name="alta_profesional"),
    path('listado-profesionales', views.ProfesionalListView.as_view(), name="listado_profesionales"),
]
