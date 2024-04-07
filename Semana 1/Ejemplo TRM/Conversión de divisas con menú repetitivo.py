

import librerias as lb

# creación de funciones para el programa principal

def ejecutar_convertir_a_dolares() -> None:
  valor = input('\n\t\tIngrese la cantidad de pesos: ')
  pesos = float(valor)

  valor = input('\n\t\tIngrese la TRM: ')
  trm = float(valor)

  dolares = lb.convertir_a_dolares(pesos, trm)

  respuesta = '\n\t\t$ {} pesos colombianos son $ {} dólares'.format(pesos, dolares)
  print(respuesta)

def ejecutar_convertir_a_pesos() -> None:
  valor = input('\n\t\tIngrese la cantidad de dólares: ')
  dolares = float(valor)
  
  valor = input('\n\t\tIngrese la TRM: ')
  trm = float(valor)

  pesos = lb.convertir_a_pesos(dolares, trm)

  respuesta = '\n\t\t$ {} dólares son $ {} pesos colombianos'.format(dolares, pesos)
  print(respuesta)

def mostrar_menu() -> str:
  print(
    '\n\t\tSeleccione una opción'
    , '\n\t\t1. Convertir de dólares a pesos'
    , '\n\t\t2. Convertir de pesos a dólares'
    , '\n\t\t3. Salir'
  )
  
  opcion = input('\n\t\tIngrese su respuesta: ') 
  return opcion

def iniciar_aplicacion() -> None:
  continuar = True

  while continuar == True:
    opcion = mostrar_menu()
    if opcion == '1':
      ejecutar_convertir_a_pesos()
    elif opcion == '2':
      ejecutar_convertir_a_dolares()
    elif opcion == '3':
      continuar = False
    else:
      print('\n\t\tLa opción seleccionada no es válida')

# programa principal

iniciar_aplicacion()

