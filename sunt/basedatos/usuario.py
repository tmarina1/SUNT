from django.db.models import query
from basedatos.models import Usuario
from datetime import datetime, date
import sqlite3

def contraseñaFuerte(clave):
    letras = 0
    numeros = 0 

    for letter in clave:
        if letter.isdigit():
            numeros += 1
        elif letter.isalpha():
            letras += 1

    if letras >= 4 and numeros >= 2:
        return True
    else:
        return False


def consultaUsuario(id):
    user = Usuario.objects.get(identificacion=id)
    info = {}

    info["identificacion"] = user.identificacion
    info["nombre"] = user.nombre
    info["apellido"] = user.apellido
    info["direccion"] = user.direccion
    info["telefono"] = user.telefono
    info["correo"] = user.correo
    info["expedicionDocumento"] = user.fechaexpediciondocumento
    info["fechaNacimiento"] = user.fechanacimiento
    print(info)
    return info

def verificarEdad(fecha_nacimiento):
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
    hoy = date.today()
    return hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))


def verificarPrevioRegistro(criterio, tipo = 'usuario'):
    query = False

    if tipo == 'usuario':
        query = Usuario.objects.filter(identificacion=criterio).exists()

    return query

def actualizarUsuario(id, tel, direccion, fecha_exp, correo):
    target = Usuario.objects.get(identificacion=id)
    target.telefono = tel
    target.direccion = direccion
    target.fechaexpediciondocumento = fecha_exp
    target.correo = correo
    target.save(update_fields=['telefono', 'direccion', 'fechaexpediciondocumento', 'correo'])

def actualizacionU():
    user = Usuario.objects.get(identificacion=id)
    if user:
        identificacion = user.identificacion
        direccion = user.direccion
        telefono = user.telefono
        correo = user.correo
        expedicionDocumento = user.fechaexpediciondocumento
        
        con = sqlite3.connect('db.sqlite3', check_same_thread=False)
        cursorObj = con.cursor()
        query = f"UPDATE basedatos_usuario SET correo='{correo}', telefono='{telefono}', direccion='{direccion}', fechaexpedicion='{expedicionDocumento}'  WHERE identificacion = '{identificacion}'"
        cursorObj = con.cursor()
        cursorObj.execute(query)