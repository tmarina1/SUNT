from basedatos.models import Licencia

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


def verificarPrevioRegistro(criterio, tipo = 'licencia'):
    query = False

    if tipo == 'licencia':
        query = Licencia.objects.filter(identificacion=criterio).exists()
    
    return query