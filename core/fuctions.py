# pylint: disable=W0311

def get_precio(peso, distancia):
  if peso <= 5:
    return(True, 11 * distancia,)
  elif peso > 5 and peso <= 10:
    return(True, 12 * distancia,)
  elif peso > 10 and peso <= 15:
    return(True, 13 * distancia,)
  elif peso > 15 and peso <= 20:
    return(True, 15 * distancia,)
  return(False, "No se puede realizar el servicio porque excede nuestro peso máximo a transportar.",)
