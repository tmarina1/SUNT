"""
sunt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('actualizacionVehiculo/', views.actualizacionVehiculo, name="actualizacionVehiculo"),
    path('registroVehiculo/', views.registroVehiculo, name="registroVehiculo"),
    path('RegistroLicencia/', views.registroLicencia, name="RegistroLicencia"),
    path('RegistroUsuarios/', views.registroUsuarios, name = "RegistroUsuarios"),
    path('Cuenta/', views.cuenta, name = "Cuenta"),
    path('Indexi/', views.indexi, name="indexi"),
    path('miInformacion/', views.miInformacion, name="miInformacion"),
    path('miVehiculo/', views.miVehiculo, name="miVehiculo"),
    path('miLicencia/', views.miLicencia, name="miLicencia"),
    path('vistaAdmin/', views.vistaAdmin, name = "vistaAdmin"),
    path('actualizacionUsuario/', views.actualizacionUsuario, name = "actualizacionUsuario"),
    path('Index/', views.logout_request, name = "cerrar_sesion"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)