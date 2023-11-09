from django.contrib import admin

from app_principal.models import Afiliado, Profesional, Plan, Especialidades, EspecialidadesProfesionales, CrearTurno

# Register your models here.
#admin.site.register(ObrasSociales)
#admin.site.register(Planes)
admin.site.register(Plan)
admin.site.register(Afiliado)
admin.site.register(Profesional)
admin.site.register(Especialidades)
admin.site.register(EspecialidadesProfesionales)
admin.site.register(CrearTurno)
