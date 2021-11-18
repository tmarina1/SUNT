
from django.contrib import messages
import basedatos.vehiculo as vehi
import basedatos.licencia as lic
import basedatos.usuario as usu
from django.shortcuts import render
from basedatos import models
import sqlite3
from django.http.response import JsonResponse
import numpy as np
import matplotlib.pyplot as plt
import os

ruta_base = os.getcwd()

# Create your views here.
def actualizacionVehiculo(request):
  if request.method == 'POST':
    placa = request.POST['Matricula']
    if vehi.verificarPrevioRegistro(placa):
      soat = request.FILES['Soat_actualizacion']
      t_mecanica = request.FILES['tecnicomecanicaActualizacion']
      prendas = request.FILES['prendas_actualizacion']
      historial = request.FILES['historial_actualizacion']
      vehi.actualizarVehiculo(placa, soat, t_mecanica, prendas, historial)
      messages.info(request,'Actualización exitosa!')
      return render(request, "actualizacionVehiculo.html") 

    else:
      messages.info(request,'La placa ingresada no se encuentra registrada')
      return render(request, "actualizacionVehiculo.html") 

  return render(request, "actualizacionVehiculo.html") 

def actualizacionUsuario(request):
  if request.method == 'POST':
    identificacion = request.POST['Identificacion']
    if usu.verificarPrevioRegistro(identificacion):
      tel = request.POST['Telefono']
      direccion = request.POST['Direccion']
      fecha_exp = request.POST['Expedicion']
      correo = request.POST['Email']
      usu.actualizarUsuario(identificacion, tel, direccion, fecha_exp, correo)
      messages.info(request,'Actualización exitosa!')
      return render(request, "actualizacionUsuario.html") 

    else:
      messages.info(request,'El usuario ingresado no se encuentra registrado')
      return render(request, "actualizacionUsuario.html") 
  return render(request, "actualizacionUsuario.html")

def registroVehiculo(request):
  if request.method == 'POST':
    matricula = request.POST['Matricula']
    modelo = request.POST['Modelo']
    tipo = request.POST['Tipo']
    soat = request.FILES['Soat']
    tecnicomecanica = request.FILES['Tecnicomecanica']
    servicio = request.POST['Servicio']
    marca = request.POST['Marca']
    vim = request.POST['Vim']
    prenda = request.FILES['Prenda']
    tipocombustible = request.POST['tipoCombustible']
    historial = request.FILES['Historial']
    cedula = request.POST['input_cedula']

    print(matricula, modelo, tipo, soat, tecnicomecanica, servicio, marca, vim, prenda, tipocombustible, historial, cedula) 

    if vehi.verificarPrevioRegistro(matricula):
      messages.info(request,'Este vehículo ya se encuentra registrado')
      return render(request, "registroVehiculo.html")

    if not usu.verificarPrevioRegistro(cedula):
      messages.info(request,'Por favor registre el usuario para poder registrar el vehiculo')
      return render(request, "registroVehiculo.html")

    if not vehi.placaValida(matricula, servicio):
      messages.info(request,'Placa inválida')
      return render(request, "registroVehiculo.html")

    else:
      user = models.Usuario.objects.get(identificacion=cedula)
      ins= models.Vehiculo(matricula = matricula, modelo= modelo, tipo= tipo, SOAT= soat,
      tecnicomecanica= tecnicomecanica, servicio=servicio, marca= marca, VIM= vim, prendas= prenda,
      tipocombustible= tipocombustible, historial= historial, idusuario = user)
      ins.save()
      messages.info(request, 'Registro exitoso!') 

  return render(request, "registroVehiculo.html") 

def registroLicencia(request):
  if request.method == 'POST':
    nombre = request.POST['Nombre']
    apellido = request.POST['Apellido']
    id = request.POST['Identificacion']
    expedicion = request.POST['Expedicion']
    vencimiento = request.POST['fechaVencimiento']
    categoria = request.POST['Categoria']
    rh = request.POST['rh']
    restricciones = request.POST['Restricciones']
    organismotransitoexpididor = request.POST['organismoExpedidor']
    fotolicencia = request.FILES['fotoLicencia']

    print(nombre, apellido, id, expedicion, vencimiento, categoria, rh, restricciones, organismotransitoexpididor ,fotolicencia)

    if lic.verificarPrevioRegistro(id):

      messages.info(request,'Este usuario ya tiene una licencia asociada')
      return render(request, "registroLicencia.html")

    if not usu.verificarPrevioRegistro(id):
      messages.info(request,'Por favor registre el usuario para poder registrar la licencia')
      return render(request, "registroLicencia.html")

  
    ins = models.Licencia(identificacion=id, nombre=nombre, apellido=apellido, fechaexpedicion=expedicion, 
    fechavencimiento = vencimiento, categoria= categoria, rh = rh, restricciones = restricciones,
    organismotransitoexpididor=organismotransitoexpididor, fotolicencia = fotolicencia)
    ins.save()
    messages.info(request, 'Registro exitoso!')

  return render(request, "registroLicencia.html") 

def registroUsuarios(request): 
  if request.method == 'POST':
    nombre = request.POST['Nombre']
    apellido = request.POST['Apellido']
    telefono = request.POST['Telefono']
    direccion = request.POST['Direccion']
    id = request.POST['Identificacion']
    expedicion = request.POST['Expedicion']
    nacimiento = request.POST['Nacimiento']
    email = request.POST['Email']
    contraseña = request.POST['Contraseña']
    
    print(nombre, apellido, telefono, direccion, id, expedicion, nacimiento, email, contraseña)


    if usu.verificarPrevioRegistro(id):
      print('Usuario ya registrado')
      messages.info(request,'Usuario ya registrado')
      return render(request, "registroUsuarios.html")

    if usu.verificarEdad(nacimiento) <= 16:
      print('Usuario no cumple edad minima')
      messages.info(request,'Usuario no cumple edad mínima')
      return render(request, "registroUsuarios.html")

    ins = models.Usuario(identificacion=id, nombre=nombre, apellido=apellido, direccion=direccion, 
    telefono=telefono, correo=email, fechaexpediciondocumento=expedicion, fechanacimiento=nacimiento, contraseña=contraseña)
    ins.save()
    messages.info(request, 'Registro exitoso!') 
    return render(request, "registroUsuarios.html") 
    
  return render(request, "registroUsuarios.html")

def indexi(request):
  return render(request, "datosCuenta.html")


login_check = False
def cuenta(request):#TODO una vez iniciado sesion, que lo lleve directamente al render de cuenta.html
  global login_check
  if login_check:
    return render(request, "datosCuenta.html")

  if request.method == 'POST':
        try:
          detalleUsuario = models.Usuario.objects.get(correo =request.POST['correo'], contraseña = request.POST['clave'])
          print("Usuario=", detalleUsuario)
          request.session['correo'] = detalleUsuario.correo
          request.session['nombre'] = detalleUsuario.nombre
          request.session['identificacion'] = detalleUsuario.identificacion
          login_check = True
          return render(request, "datosCuenta.html")

        except models.Usuario.DoesNotExist as e:
          messages.success(request, "Nombre de usuario y/o contraseña invalidos")

  return render(request, "cuenta.html")

def logout_request(request):#TODO Esto si hace algo? revisar credenciales una ves se finalice el logout
      global login_check
      messages.info(request,"Se ha cerrado la sesión")
      login_check = False
      return render(request, "index.html")


def miInformacion(request):
  cedula = request.session['identificacion']
  info_usuario = usu.consultaUsuario(cedula)

  return render(request, "miInformacion.html", {"info_usuario": info_usuario})

def miVehiculo(request):
  cedula = request.session['identificacion']
  info_vehiculo= vehi.consultaVehiculo(cedula)
  print(info_vehiculo)
  return render(request, "miVehiculo.html", {"info_vehiculo":info_vehiculo})

def miLicencia(request):
  cedula = request.session['identificacion']
  try:
    info_licencia = lic.consultaLicencia(cedula)
  except:
    info_licencia = None
  return render(request, "miLicencia.html", {"info_licencia": info_licencia})

con = sqlite3.connect('db.sqlite3', check_same_thread=False)
cursorObj = con.cursor()

def vistaAdmin(request):
  separar(con)
  separargrafica2(con)
  separargrafica3(con)
  querys = {'consulta1': querysEdades(con),'consulta2':querysPersonas(con),'consulta3':querysVehiculos(con),'consulta4':querysLicencias(con)}
  return render(request, "vistaAdmin.html",{"querys": querys}) 

def separar(con):
  datos = sql_fetch(con)
  list1 = []
  list2 = []
  for row in datos:
    print(row)
    list1.append(row[0])
    list2.append(row[1])

  list1 = list(map(str, list1))

  plt.bar(list1, list2)
  plt.ylabel('Cantidad de usuarios')
  plt.xlabel('Edades de los usuarios')
  plt.title('Cantidad de personas por edades')
  plt.savefig(f"{ruta_base}\\static\\sunt\\imagenes\\grafica.png")
  plt.close()

def separargrafica2(con):
    datos1 = consulta_db2(con)
    list12 = []
    list22 = []
    for row in datos1:
      list12.append(row[0])
      list22.append(row[1])
    list12 = list(map(str, list12))
    print(list12)
    print(list22)
    plt.bar(list12, list22)
    plt.ylabel('Cantidad de licencias')
    plt.xlabel('Categoria')
    plt.title('Categoria de las licencias')
    plt.savefig(f"{ruta_base}\\static\\sunt\\imagenes\\grafica2.png")
    plt.close()

def separargrafica3(con):
    datos2 = consulta_db3(con)
    list3 = []
    list4 = []
    for row in datos2:
      list3.append(row[0])
      list4.append(row[1])
    list3 = list(map(str, list3))
    print(list3)
    print(list4)
    plt.bar(list3, list4)
    plt.ylabel('Cantidad de Vehiculos')
    plt.xlabel('Tipo')
    plt.title('Tipos de vehiculos')
    plt.savefig(f"{ruta_base}\\static\\sunt\\imagenes\\grafica3.png")
    plt.close()

def sql_fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute('select (DateTime() - fechanacimiento) as edad,Count(DateTime() - fechanacimiento) as cantidad from basedatos_usuario group by (DateTime() - fechanacimiento)')
    rows = cursorObj.fetchall()
    return rows

def consulta_db2(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT categoria, count(*) as Cantidad FROM basedatos_licencia GROUP BY categoria;')
    rows = cursorObj.fetchall()
    return rows   

def consulta_db3(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT tipo, count(*) as Cantidad FROM basedatos_vehiculo GROUP BY tipo;')
    rows = cursorObj.fetchall()
    return rows    

def querysEdades(con):
  mensaje =""
  cursorObj = con.cursor()
  cursorObj.execute('select (DateTime() - fechanacimiento) as edad,Count(DateTime() - fechanacimiento) as cantidad from basedatos_usuario group by (DateTime() - fechanacimiento)')
  mensaje = cursorObj.fetchall()
  mensaje = str(mensaje)
  mensaje = mensaje.replace(mensaje[0], "")
  mensaje = mensaje.replace(mensaje[len(mensaje)-1], "")
  return mensaje

def querysPersonas(con):
  mensaje =""
  cursorObj = con.cursor()
  cursorObj.execute('select Count(*) from basedatos_usuario')
  mensaje = cursorObj.fetchall()
  mensaje = str(mensaje)
  mensaje = mensaje.replace(mensaje[0], "")
  mensaje = mensaje.replace(mensaje[0], "")
  mensaje = mensaje.replace(mensaje[len(mensaje)-1], "")
  mensaje = mensaje.replace(mensaje[len(mensaje)-2], "")
  mensaje = mensaje.replace(mensaje[len(mensaje)-3], "")
  return mensaje

def querysVehiculos(con):
  mensaje =""
  cursorObj = con.cursor()
  cursorObj.execute('select Count(*) from basedatos_vehiculo')
  mensaje = cursorObj.fetchall()
  mensaje = str(mensaje)
  mensaje = mensaje.replace(mensaje[0], "")
  mensaje = mensaje.replace(mensaje[0], "")
  mensaje = mensaje.replace(mensaje[len(mensaje)-1], "")
  mensaje = mensaje.replace(mensaje[len(mensaje)-2], "")
  mensaje = mensaje.replace(mensaje[len(mensaje)-3], "")
  return mensaje

def querysLicencias(con):
  mensaje =""
  cursorObj = con.cursor()
  cursorObj.execute('select Count(*) from basedatos_licencia')
  mensaje = cursorObj.fetchall()
  mensaje = str(mensaje)
  mensaje = mensaje.replace(mensaje[0], "")
  mensaje = mensaje.replace(mensaje[0], "")
  mensaje = mensaje.replace(mensaje[len(mensaje)-1], "")
  mensaje = mensaje.replace(mensaje[len(mensaje)-2], "")
  mensaje = mensaje.replace(mensaje[len(mensaje)-3], "")
  return mensaje



