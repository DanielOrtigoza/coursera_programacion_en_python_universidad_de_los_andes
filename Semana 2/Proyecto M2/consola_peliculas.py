"""
Ejercicio nivel 2: Agenda de peliculas.
Modulo de interacci0n por consola.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.
@author: Cupi2
"""

import modulo_peliculas as mod
import random as rm

def mostrar_informacion_pelicula(pelicula: dict)-> None:
    """Imprime los detalles de la pelicula
    Parametros:
        pelicula(dict): La pelicula de la cual se van a mostrar los detalles
        El diccionario que representa una pelicula contiene las siguientes parejas de
        llave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula
            - dia (str): Indica que dia de la semana se planea ver la pelicula
    """       
    nombre = pelicula["nombre"]
    genero = pelicula["genero"]
    duracion = pelicula["duracion"]
    anio = pelicula["anio"]
    clasificacion = pelicula["clasificacion"]
    hora = pelicula["hora"]
    dia = pelicula["dia"]
    
    print("Nombre: " + nombre + " - Anio: " + str(anio) + " - Duracion: " + str(duracion) + "  mins" )
    print("Genero: " + genero + " - Clasificacion: " + clasificacion)
    
    if (hora//100 < 10):
        hora_formato = "0"+ str(hora//100)
    else:
        hora_formato = str(hora//100)
    
    if (hora%100 < 10):
        min_formato = "0"+ str(hora%100)
    else:
        min_formato = str(hora%100)

    print("Dia: " + dia + " Hora: " + hora_formato + ":" + min_formato)

def ejecutar_encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:
    """Ejecuta la opcion de encontrar la pelicula mas larga.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """
    pelicula_mas_larga = mod.encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)
    print("\n\t\tLa pelicula con mayor duracion es", pelicula_mas_larga["nombre"], "con una duracion de", pelicula_mas_larga["duracion"], "minutos.")
    print("\n\t\tFicha completa de la pelicula:", pelicula_mas_larga)
    print("\n")
    
def ejecutar_consultar_duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:
    """Ejecuta la opcion de consultar la duracion promedio de las peliculas.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """
    duracion_promedio_peliculas = mod.duracion_promedio_peliculas(p1, p2, p3, p4, p5)
    print("\n\t\tLa cantidad promedio de duracion de todas las peliculas presentes en el catalogo es:", duracion_promedio_peliculas + ". " + "Formato en el cual se esta representando la informacion \"HH:MM\". ")
    print("\n")
    
def ejecutar_encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:
    """ Ejecuta la opcion de buscar peliculas de estreno. Esto es: las peliculas que sean 
        mas recientes que un anio dado.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """
    anio = int(input("\n\t\tIngrese el anio de estreno de la pelicula: "))
    encontrar_estrenos = mod.encontrar_estrenos(p1, p2, p3, p4, p5, anio)
    print("\n\t\tLa(s) pelicula(s) estrenada(s) despues de el anio", anio, "es/son:" , encontrar_estrenos)
    print("\n")
    
def ejecutar_cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:
    """Ejecuta la opcion de consultar cuantas peliculas de la agenda tienen clasificacion
    18+.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """
    peliculas_18_mas = mod.cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)
    print("\n\t\tEl numero de peliculas con la clasificacion 18+ son:", peliculas_18_mas)
    print("\n")
    
def ejecutar_reagendar_pelicula(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:
    """Ejecuta la opcion de reagendar una pelicula
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """
    print("\nReagendar una pelicula de la agenda")

    nombre = input("\n\t\tIngrese el nombre de la pelicula que desea reagendar: ").title()
    pelicula = mod.encontrar_pelicula(nombre,p1,p2,p3,p4,p5)
    
    if pelicula is None:
        print("\n\t\tNo hay ninguna pelicula con este nombre")
    else:
        
        nuevo_dia = input("\t\tIngrese el dia al que desea reprogramar la pelicual: ").lower()
        
        control_hora = input("\t\t¿Desea tener control sobre la hora a cambiar la emision de la pelicula (si/no):? ").lower()
        
        if control_hora == "si":
            control_hora = True
        elif control_hora == "no":
            control_hora = False
        
        if control_hora == True:
            nueva_hora = int(input("\t\tIngrese la hora para el que desea reprogramar la pelicula: "))
        else:
            nueva_hora = rm.randrange(0000, 2400)
        
        control_horario = input("\t\t¿Desea tener control sobre el horario de la pelicula (si/no):? ").lower()
        
        if control_horario == "si":
            if pelicula["genero"].find("Documental") != -1 and nueva_hora >= 2200:
                print("\n\t\tNo se pudo realizar el cambio, la pelicula seleccionada es de tipo", pelicula.get("genero"), "y el horario al que fue reprogramado fue superior a las 10:00 pm.")
            elif pelicula["genero"].find("Drama") != -1 and nuevo_dia == "viernes":
                print("\n\t\tNo se pudo realizar el cambio, la pelicula seleccionada es de tipo", pelicula.get("genero"), "y el dia seleccionado es", nuevo_dia.capitalize() + ".")
            elif (nuevo_dia == "lunes" or nuevo_dia == "martes" or nuevo_dia == "miercoles" or nuevo_dia == "jueves" or nuevo_dia == "viernes") and (nueva_hora >= 2300 or nueva_hora <= 600):
                print("\n\t\tNo se pudo realizar el cambio, el dia seleccionado es entre semana (lunes a viernes) y la hora selesccionados es muy tarde (despues de las 11:00 pm) o muy temprano (antes de las 6:00 am).")
            else:
                x = mod.reagendar_pelicula(pelicula, nueva_hora, nuevo_dia, control_horario, p1, p2, p3, p4, p5)
                if x == True:
                    print("\n\t\tCambio realizado con exito. Podra ver el cambio reflejado en \"Mi agenda de peliculas para la semana de receso\".")
                else:
                    print("\n\t\tNo se pudo reprogramar la pelicula. El horario escogido fue", nueva_hora, "cruzandose con otra pelicula asignada para ese dia.")
        if control_horario == "no":
            x = mod.reagendar_pelicula(pelicula, nueva_hora, nuevo_dia, control_horario, p1, p2, p3, p4, p5)
            if x == True:
                print("\n\t\tCambio realizado con exito. Podra ver el cambio reflejado en \"Mi agenda de peliculas para la semana de receso\".")
            else:
                print("\n\t\tNo se pudo reprogramar la pelicula. El horario escogido fue", nueva_hora, "cruzandose con otra pelicula asignada para ese dia.")
    
    print("\n")
def ejecutar_decidir_invitar(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:
    """Ejecuta la opcion de decidir si se puede invitar a alguien a ver una pelicula o no.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """
    print("\nDecidir si se puede invitar a alguien a ver una pelicula")

    nom_peli = input("\n\t\tIngrese el nombre de la pelicula: ").title()
    pelicula = mod.encontrar_pelicula(nom_peli,p1,p2,p3,p4,p5)

    if pelicula is None:
        print("\n\t\tNo hay ninguna pelicula con este nombre")
    
    else:
        edad_invitado = int(input("\t\tIngrese la edad de el invitado: "))
        autorizacion_padres = input("\t\t¿La persona invitada tiene autorizacion de sus padres para ver la pelicula (si/no): ?").lower()
        
        if autorizacion_padres  == "si":
            autorizacion_padres  = True
        elif autorizacion_padres  == "no":
            autorizacion_padres  = False
        
        x = mod.decidir_invitar(pelicula, edad_invitado, autorizacion_padres)
        
        if x == True:
            print("\n\t\tEl invitado puede ver la pelicula.")
        else:
            print("\n\t\tEl invitado no pueder ver la pelicula.")
    print("\n")
def iniciar_aplicacion():
    """Inicia la ejecución de la aplicación por consola.
    Esta funcion primero crea las cinco peliculas que se van a manejar en la agenda.
    Luego la funcion le muestra el menu al usuario y espera a que seleccione una opcion.
    Esta operacion se repite hasta que el usuario seleccione la opcion de salir.
    """
    pelicula1 = mod.crear_pelicula("Shrek",  "Familiar, Comedia", 92, 2001, 'Todos', 1700, "Viernes")
    pelicula2 = mod.crear_pelicula("Get Out",  "Suspenso, Terror", 104, 2017, '18+', 2330, "Sabado")  
    pelicula3 = mod.crear_pelicula("Icarus",  "Documental, Suspenso", 122, 2017, '18+', 800, "Domingo")
    pelicula4 = mod.crear_pelicula("Inception",  "Acción, Drama", 148, 2010, '13+', 1300, "Lunes")
    pelicula5 = mod.crear_pelicula("The Empire Strikes Back",  "Familiar, Ciencia-Ficción", 124, 1980, '7+', 1415, "Miercoles")
    
    ejecutando = True
    while ejecutando:            
        print("\n\nMi agenda de peliculas para la semana de receso" +"\n"+("-"*50))
        print("Pelicula 1")
        mostrar_informacion_pelicula(pelicula1)
        print("-"*50)
        
        print("Pelicula 2")
        mostrar_informacion_pelicula(pelicula2)
        print("-"*50)
        
        print("Pelicula 3")
        mostrar_informacion_pelicula(pelicula3)
        print("-"*50)
        
        print("Pelicula 4")
        mostrar_informacion_pelicula(pelicula4)
        print("-"*50)
        
        print("Pelicula 5")
        mostrar_informacion_pelicula(pelicula5)
        print("-"*50)
        
        ejecutando = mostrar_menu_aplicacion(pelicula1, pelicula2, pelicula3, pelicula4, pelicula5)

        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")

def mostrar_menu_aplicacion(p1: dict, p2: dict, p3: dict, p4:dict, p5:dict) -> bool:
    """Le muestra al usuario las opciones de ejecución disponibles.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorno:
        Esta funcion retorna True si el usuario selecciono una opcion diferente 
        a la opcion que le permite salir de la aplicacion.
        Esta funcion retorna False si el usuario selecciono la opción para salir 
        de la aplicacion.
    """
    print("Menu de opciones")
    print(" 1 - Consultar pelicula mas larga")
    print(" 2 - Consultar duracion promedio de las peliculas")
    print(" 3 - Consultar peliculas de estreno")
    print(" 4 - Consultar cuantas peliculas tienen clasificacion 18+")
    print(" 5 - Reagendar pelicula")
    print(" 6 - Verificar si se puede invitar a alguien")    
    print(" 7 - Salir de la aplicacion")

    opcion_elegida = input("Ingrese la opcion que desea ejecutar: ").strip()
    
    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)
    elif opcion_elegida == "2":
        ejecutar_consultar_duracion_promedio_peliculas(p1, p2, p3, p4, p5)
    elif opcion_elegida == "3":
        ejecutar_encontrar_estrenos(p1, p2, p3, p4, p5)
    elif opcion_elegida == "4":
        ejecutar_cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)        
    elif opcion_elegida == "5":
        ejecutar_reagendar_pelicula(p1, p2, p3, p4, p5) 
    elif opcion_elegida == "6":
        ejecutar_decidir_invitar(p1, p2, p3, p4, p5) 
    elif opcion_elegida == "7":
        continuar_ejecutando = False
    else:
        print("La opcion " + opcion_elegida + " no es una opcion valida.")
    
    return continuar_ejecutando

iniciar_aplicacion()