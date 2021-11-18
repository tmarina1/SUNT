import datetime
from basedatos.models import Usuario, Licencia, Vehiculo
from datetime import datetime, date

#Para no guardar la imagen en la base de datos
def extraerNombreArchivo(archivo):

    pass

def verificarEdad(fecha_nacimiento):
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
    hoy = date.today()
    return hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

def verificarPrevioRegistro(tipo, criterio):
    query = False

    if tipo == 'usuario':
        query = Usuario.objects.filter(identificacion=criterio).exists()

    if tipo == 'licencia':
        query = Licencia.objects.filter(identificacion=criterio).exists()
    
    if tipo == 'vehiculo':
        query = Vehiculo.objects.filter(matricula=criterio).exists()

    print(Usuario.objects.filter(identificacion=criterio))
    return query

#borrar
def usuarioExiste(id):
    q = Usuario.objects.filter(identificacion=id)
    return q.exists()

def placaValida(placa, tipo):
    letras = 0 
    numeros = 0
    
    for letter in placa:
        if letter.isdigit():
            numeros += 1
        elif letter.isalpha():
            letras += 1

    if tipo == 'Particular' or tipo == 'Público':
        return letras == 3 and numeros == 3
    
    if tipo == 'Diplomático':
        return letras == 2 and numeros == 4
    
    if tipo == 'Carga':
        return letras == 1 and numeros == 4
    


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
    

def generarID():
    pass

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

def consultaVehiculo(id_usuario):
    user = Usuario.objects.get(identificacion=id_usuario)
    vehc = Vehiculo.objects.filter(idusuario = user)
    return vehc

def consultaLicencia(id):
    lic = Licencia.objects.get(identificacion=id)
    info = {}
    info["identificacion"] = lic.identificacion
    info["fechaexpedicion"] = lic.fechaexpedicion
    info["fechavencimiento"] = lic.fechavencimiento
    info["categoria"] = lic.categoria
    info["rh"] = lic.rh
    info["nombre"] = lic.nombre
    info["apellido"] = lic.apellido
    info["restricciones"] = lic.restricciones
    info["organismotransitoexpedidor"] = lic.organismotransitoexpididor #TODO corregir ortografia
    info["fotolicencia"] = lic.fotolicencia
    print(info)
    return info