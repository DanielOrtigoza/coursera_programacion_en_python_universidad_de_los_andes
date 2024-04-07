
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


compania_fun()

