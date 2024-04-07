

import librerias as lb

def ejecutar_convertir_a_dolares(trm: float) -> None:
  valor = input('\n\t\tIngrese la cantidad de pesos: ')
  pesos = float(valor)
  dolares = lb.convertir_a_dolares(pesos, trm)

  respuesta = '\n\t\t$ {} pesos colombianos son $ {} dolares'.format(pesos, dolares)
  print(respuesta)

def ejecutar_convertir_a_pesos(trm: float) -> None:
  valor = input('\n\t\tIngrese la cantidad de dolares: ')
  dolares = float(valor)
  pesos = lb.convertir_a_pesos(dolares, trm)

  respuesta = '\n\t\t$ {} dolares son $ {} pesos colombianos'.format(dolares, pesos)
  print(respuesta)

def iniciar_aplicacion() -> None:
  valor = input('\n\t\tIngrese la TRM: ')
  trm = float(valor)

  ejecutar_convertir_a_dolares(trm)
  ejecutar_convertir_a_pesos(trm)

iniciar_aplicacion()

