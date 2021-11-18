from django.contrib import admin
from .models import Licencia, Vehiculo, Usuario, Tramite, Administrador

# Register your models here.

class LicenciaAdmin(admin.ModelAdmin):
  readonly_fields = ()

class UsuarioAdmin(admin.ModelAdmin):
  readonly_fields = ()

class VehiculoAdmin(admin.ModelAdmin):
  readonly_fields = ()

class TramiteAdmin(admin.ModelAdmin):
  readonly_fields = ()

class AdministradorAdmin(admin.ModelAdmin):
  readonly_fields = ()

admin.site.register(Licencia, LicenciaAdmin)  
admin.site.register(Usuario, UsuarioAdmin)  
admin.site.register(Vehiculo, VehiculoAdmin)  
admin.site.register(Tramite, TramiteAdmin)  
admin.site.register(Administrador, AdministradorAdmin)  