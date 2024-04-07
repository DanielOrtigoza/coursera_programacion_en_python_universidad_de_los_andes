
# librerias de conversión de divisas

def convertir_a_dolares(pesos: float, trm: float) -> float:
  """
  Función la cual devuelve cuandos dolares son cierta cantidad de pesos colombianos con una trm especificada en pesos colombianos.

  Parameters
  ----------
  pesos: valor de pesos colombianos a convertir en dolares
  trm: trm en pesos colombianos 

  Returns
  -------
  dolares: dolares

  """

  dolares = (1 / trm) * pesos

  return dolares

def convertir_a_pesos(dolares: float, trm: float) -> float:
  """
  Función la cual devuelve cuandos pesos son cierta cantidad de dolares con una trm especificada en pesos colombianos.

  Parameters
  ----------
  dolares: valor de dolares a convertir en pesos colombianos
  trm: trm en pesos colombianos 

  Returns
  -------
  pesos: pesos colombianos finales

  """

  pesos = (trm / 1)  * dolares

  return pesos

