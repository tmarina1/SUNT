"""sunt URL Configuration

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
from django.urls import path, include
from sunt.views import index
from sunt.views import sobrenosotros
from sunt.views import normas
from sunt.views import tramites
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('sobrenosotros/', sobrenosotros, name="sobrenosotros"),
    #path('cuenta/', cuenta, name="cuenta"),
    path('tramites/', tramites, name="tramites"),
    path('normas/', normas, name = "normas"),
    #path('basedatos/',include('basedatos.urls')),
    path('', include('basedatos.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('regvehiculo/', regvehiculo, name="regvehiculo")
    #path('actualizacionVe/',actualizacionVe, name="actualizacionVe"),
]
