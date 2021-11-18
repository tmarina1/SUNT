from basedatos.models import Usuario, Vehiculo

def placaValida(placa, tipo):
    letras = 0 
    numeros = 0
    
    for letter in placa:
        if letter.isdigit():
            numeros += 1
        elif letter.isalpha():
            letras += 1

    if tipo == 'Particular' or tipo == 'particular' or tipo == 'Público' or tipo == 'público':
        return letras == 3 and numeros == 3
    
    if tipo == 'Diplomático':
        return letras == 2 and numeros == 4
    
    if tipo == 'Carga':
        return letras == 1 and numeros == 4


def consultaVehiculo(id_usuario):
    user = Usuario.objects.get(identificacion=id_usuario)
    vehc = Vehiculo.objects.filter(idusuario = user)
    return vehc


def verificarPrevioRegistro(criterio, tipo='vehiculo'):
    query = False
    
    if tipo == 'vehiculo':
        query = Vehiculo.objects.filter(matricula=criterio).exists()

    return query

def actualizarVehiculo(placa, soat, t_mecanica, prendas, historial):
    target = Vehiculo.objects.get(matricula=placa)
    target.SOAT = soat
    target.tecnicomecanica = t_mecanica
    target.prendas = prendas
    target.historial = historial
    target.save(update_fields=['SOAT', 'tecnicomecanica', 'prendas', 'historial'])