





def compania_fun() -> str:
  print(
    '\n\t\tSeleccione una opción'
    , '\n\t\t1. ALAS'
    , '\n\t\t2. VOLAR'
  )

  opcion = int(input('\n\t\tIngrese su respuesta: '))

  if opcion == 1:
    valor = 'ALAS'
  elif opcion == 2:
    valor = 'VOLAR'
  else:
    valor = 'valor ingresado incorrecto'
    print(valor)

  return valor



def temporada_alta_fun() -> bool:
  print(
    '\n\t\t¿Es temporada alta?'
    , '\n\t\tSi'
    , '\n\t\tNo'
  )

  opcion = input('\n\t\tIngrese su respuesta: ')

  if opcion == 'Si':
    valor = True
  elif opcion == 'No':
    valor = False
  else:
    valor = 'valor ingresado incorrecto'
    print(valor)

  return valor



def estudiante_fun() -> bool:
  print(
    '\n\t\t¿Es estudiante?'
    , '\n\t\tSi'
    , '\n\t\tNo'
  )

  opcion = input('\n\t\tIngrese su respuesta: ')

  if opcion == 'Si':
    valor = True
  elif opcion == 'No':
    valor = False
  else:
    valor = 'valor ingresado incorrecto'
    print(valor)

  return valor


# def calcular_precio_pasaje(compañia: str, edad: int, temporada_alta: bool, estudiante: bool) -> int:
def calcular_precio_pasaje(edad: int) -> None:
  
  precio_pasaje = 5000000.00

  compania = compania_fun()
  temporada_alta = temporada_alta_fun()
  estudiante = estudiante_fun()

  if compania == 'ALAS':
    if temporada_alta == True:
      precio_pasaje = precio_pasaje + (precio_pasaje * 0.3)
    elif temporada_alta == False and edad >= 18 and estudiante == True:
      precio_pasaje = precio_pasaje - (precio_pasaje * 0.1)

  elif compania == 'VOLAR':
    if temporada_alta == True:
      precio_pasaje = precio_pasaje + (precio_pasaje * 0.2)
    elif edad > 60:
      precio_pasaje = precio_pasaje + 100000.00
  
  if edad < 18:
    precio_pasaje = precio_pasaje - (precio_pasaje * 0.5)

  respuesta = '\n\t\tEl precio del pasaje es de $ {} COP'.format(precio_pasaje)
  print(respuesta)

edad = int(input('\n\t\tIngrese la edad: '))
calcular_precio_pasaje(edad)


