from django.db import models
import datetime
import os

def filepath(request, filename):
  old_filename = filename
  timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
  filename = "%s%s" % (timeNow, old_filename)
  return os.path.join('uploads/, filename')

# Create your models here.
class Licencia(models.Model):
  identificacion = models.CharField(max_length = 15)
  fechaexpedicion = models.DateField()
  fechavencimiento = models.DateField()
  categoria = models.CharField(max_length = 10)
  rh = models.CharField(max_length = 3) 
  nombre = models.CharField(max_length = 30)
  apellido = models.CharField(max_length = 30) 
  restricciones = models.CharField(max_length = 30)
  organismotransitoexpididor = models.CharField(max_length = 20)
  fotolicencia = models.ImageField(upload_to = 'images/')#'sunt/basedatos/archivoscargados')
  class Meta:
    verbose_name = "licencia"
    verbose_name_plural = "licencias" 

#Hace falta contraseña
class Usuario(models.Model):
  identificacion = models.CharField(max_length = 10)
  nombre = models.CharField(max_length = 30)
  apellido = models.CharField(max_length = 30)
  direccion = models.CharField(max_length = 50)
  telefono = models.CharField(max_length = 7)
  correo = models.EmailField()
  fechaexpediciondocumento = models.DateField()
  fechanacimiento = models.DateField()
  contraseña = models.CharField(max_length = 10)
  idlicencia = models.ForeignKey(Licencia,on_delete = models.CASCADE, null=True, blank=True)
  class Meta:
    verbose_name = "usuario"
    verbose_name_plural = "usuarios"

#idusuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)

class Vehiculo(models.Model):
  matricula = models.CharField(max_length = 5)
  modelo = models.CharField(max_length = 20)
  tipo = models.CharField(max_length = 20)
  SOAT = models.FileField(upload_to = 'archivos/')
  tecnicomecanica = models.FileField(upload_to = 'archivos/')
  servicio = models.CharField(max_length= 20)
  marca = models.CharField(max_length = 20)
  VIM = models.IntegerField()  
  prendas = models.FileField(upload_to = 'archivos/')
  tipocombustible = models.CharField(max_length = 15)
  historial = models.FileField(upload_to = 'archivos/')
  idusuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
  class Meta:
    verbose_name = "vehiculo"
    verbose_name_plural = "vehiculos"

class Tramite(models.Model):
    numtramite = models.CharField(max_length = 15)
    nombretramite = models.CharField(max_length = 15)
    tipo = models.CharField(max_length = 15)
    idusuario = models.CharField(max_length = 15)
    idvehiculo = models.CharField(max_length = 15)
    duracion = models.CharField(max_length = 15)
    idusuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    idvehiculo = models.ForeignKey(Vehiculo, on_delete = models.CASCADE, null=True)
    class Meta:
      verbose_name = "tramite"
      verbose_name_plural = "tramites"

class Administrador(models.Model):
  nombre = models.CharField(max_length = 15)
  apellidos = models.CharField(max_length = 15)
  idadministrador = models.CharField(max_length = 15)
  cargo = models.CharField(max_length = 15)  
  idtramite = models.ForeignKey(Tramite, on_delete = models.CASCADE)
  class Meta:
    verbose_name = "administrador"
    verbose_name_plural = "administradores"      