"""
Ejercicio nivel 2: Agenda de peliculas.
Módulo de cálculos.

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

NOTA IMPORTANTE PARA TENER EN CUENTA EN TODAS LAS FUNCIONES DE ESTE MODULO:
        Los diccionarios de pelicula tienen las siguientes parejas de clave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula
            - dia (str): Indica que día de la semana se planea ver la película
"""

def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int, 
                  clasificacion: str, hora: int, dia: str) -> dict:
    """Crea un diccionario que representa una nueva película con toda su información 
       inicializada.
    Parámetros:
        nombre (str): Nombre de la pelicula agendada.
        genero (str): Generos de la pelicula separados por comas.
        duracion (int): Duracion en minutos de la pelicula
        anio (int): Anio de estreno de la pelicula
        clasificacion (str): Clasificacion de restriccion por edad
        hora (int): Hora a la cual se planea ver la pelicula, esta debe estar entre 
                    0 y 2359
        dia (str): Dia de la semana en el cual se planea ver la pelicula.
    Retorna:
        dict: Diccionario con los datos de la pelicula
    """
    
    nueva_pelicula = {}
    nueva_pelicula["nombre"] = nombre
    nueva_pelicula["genero"] = genero
    nueva_pelicula["duracion"] = duracion
    nueva_pelicula["anio"] = anio
    nueva_pelicula["clasificacion"] = clasificacion
    nueva_pelicula["hora"] = hora
    nueva_pelicula["dia"] = dia
    return nueva_pelicula

def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    """Encuentra en cual de los 5 diccionarios que se pasan por parametro esta la 
       pelicula cuyo nombre es dado por parametro.
       Si no se encuentra la pelicula se debe retornar None.
    Parametros:
        nombre_pelicula (str): El nombre de la pelicula que se desea encontrar.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: Diccionario de la pelicula cuyo nombre fue dado por parametro. 
        None si no se encuentra una pelicula con ese nombre.
    """
    
    nombre_pelicula_1 = p1["nombre"]
    nombre_pelicula_2 = p2["nombre"]
    nombre_pelicula_3 = p3["nombre"]
    nombre_pelicula_4 = p4["nombre"]
    nombre_pelicula_5 = p5["nombre"]
    
    x = {}
    
    if nombre_pelicula_1 == nombre_pelicula:
        x = p1
    elif nombre_pelicula_2 == nombre_pelicula:
        x = p2
    elif nombre_pelicula_3 == nombre_pelicula:
        x = p3
    elif nombre_pelicula_4 == nombre_pelicula:
        x = p4
    elif nombre_pelicula_5 == nombre_pelicula:
        x = p5
    else:
        x = None
    
    return x

def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    """Encuentra la pelicula de mayor duracion entre las peliculas recibidas por
       parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: El diccionario de la pelicula de mayor duracion
    """
    
    duracion_pelicula_1 = p1["duracion"]
    duracion_pelicula_2 = p2["duracion"]
    duracion_pelicula_3 = p3["duracion"]
    duracion_pelicula_4 = p4["duracion"]
    duracion_pelicula_5 = p5["duracion"]
    
    mayor = p1
    
    if duracion_pelicula_2 > duracion_pelicula_1:
        mayor = p2
    if duracion_pelicula_3 > duracion_pelicula_2:
        mayor = p3
    if duracion_pelicula_4 > duracion_pelicula_3:
        mayor = p4
    if duracion_pelicula_5 > duracion_pelicula_4:
        mayor = p5
    
    return mayor

def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> str:
    """Calcula la duracion promedio de las peliculas que entran por parametro. 
       Esto es, la duración total de todas las peliculas dividida sobre el numero de peliculas. 
       Retorna la duracion promedio en una cadena de formato 'HH:MM' ignorando los posibles decimales.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        str: la duracion promedio de las peliculas en formato 'HH:MM'
    """
    
    duracion_pelicula_1 = p1["duracion"]
    duracion_pelicula_2 = p2["duracion"]
    duracion_pelicula_3 = p3["duracion"]
    duracion_pelicula_4 = p4["duracion"]
    duracion_pelicula_5 = p5["duracion"]
    
    duración_promedio = (duracion_pelicula_1 + duracion_pelicula_2 + duracion_pelicula_3 + duracion_pelicula_4 + duracion_pelicula_5 ) / 5
    
    horas = int(duración_promedio / 60)
    minutos = int(duración_promedio - (horas * 60))
    
    return str(horas) + ":" + str(minutos)

def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio: int) -> str:
    """Busca entre las peliculas cuales tienen como anio de estreno una fecha estrictamente
       posterior a la recibida por parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
        anio (int): Anio limite para considerar la pelicula como estreno.
    Retorna:
        str: Una cadena con el nombre de la pelicula estrenada posteriormente a la fecha recibida. 
        Si hay mas de una pelicula, entonces se retornan los nombres de todas las peliculas 
        encontradas separadas por comas. Si ninguna pelicula coincide, retorna "Ninguna".
    """
    
    anio_estreno_pelicula_1 = p1["anio"]
    anio_estreno_pelicula_2 = p2["anio"]
    anio_estreno_pelicula_3 = p3["anio"]
    anio_estreno_pelicula_4 = p4["anio"]
    anio_estreno_pelicula_5 = p5["anio"]
    
    if anio_estreno_pelicula_1 > anio:
        pelicula1 = p1["nombre"]
    else:
        pelicula1 = None
        
    if anio_estreno_pelicula_2 > anio:
        pelicula2 = p2["nombre"]
    else:
        pelicula2 = None
        
    if anio_estreno_pelicula_3 > anio:
        pelicula3 = p3["nombre"]
    else:
        pelicula3 = None
        
    if anio_estreno_pelicula_4 > anio:
        pelicula4 = p4["nombre"]
    else:
        pelicula4 = None
        
    if anio_estreno_pelicula_5 > anio:
        pelicula5 = p5["nombre"]
    else:
        pelicula5 = None
    
    if pelicula1 is None and pelicula2 is None and pelicula3 is None and pelicula4 is None and pelicula5 is None:
        mensaje = "Ninguna"
    
    if pelicula1 is not None and pelicula2 is None and pelicula3 is None and pelicula4 is None and pelicula5 is None:
        mensaje = pelicula1
    
    if pelicula1 is None and pelicula2 is not None and pelicula3 is None and pelicula4 is None and pelicula5 is None:
        mensaje = pelicula2
    
    if pelicula1 is None and pelicula2 is None and pelicula3 is not None and pelicula4 is None and pelicula5 is None:
        mensaje = pelicula3
        
    if pelicula1 is None and pelicula2 is None and pelicula3 is None and pelicula4 is not None and pelicula5 is None:
        mensaje = pelicula4
    
    if pelicula1 is None and pelicula2 is None and pelicula3 is None and pelicula4 is None and pelicula5 is not None:
        mensaje = pelicula5
    
    if pelicula1 is not None and pelicula2 is not None and pelicula3 is None and pelicula4 is None and pelicula5 is None:
        mensaje = pelicula1 + ", " + pelicula2
    
    if pelicula1 is not None and pelicula2 is None and pelicula3 is not None and pelicula4 is None and pelicula5 is None:
        mensaje = pelicula1 + ", " + pelicula3
    
    if pelicula1 is not None and pelicula2 is None and pelicula3 is None and pelicula4 is not None and pelicula5 is None:
        mensaje = pelicula1 + ", " + pelicula4
    
    if pelicula1 is not None and pelicula2 is None and pelicula3 is None and pelicula4 is None and pelicula5 is not None:
        mensaje = pelicula1 + ", " + pelicula5
    
    if pelicula1 is None and pelicula2 is not None and pelicula3 is not None and pelicula4 is None and pelicula5 is None:
        mensaje = pelicula2 + ", " + pelicula3
    
    if pelicula1 is None and pelicula2 is not None and pelicula3 is None and pelicula4 is not None and pelicula5 is None:
        mensaje = pelicula2 + ", " + pelicula4
    
    if pelicula1 is None and pelicula2 is not None and pelicula3 is None and pelicula4 is None and pelicula5 is not None:
        mensaje = pelicula2 + ", " + pelicula5
    
    if pelicula1 is None and pelicula2 is None and pelicula3 is not None and pelicula4 is not None and pelicula5 is None:
        mensaje = pelicula3 + ", " + pelicula4
        
    if pelicula1 is None and pelicula2 is None and pelicula3 is not None and pelicula4 is None and pelicula5 is not None:
        mensaje = pelicula3 + ", " + pelicula5
    
    if pelicula1 is None and pelicula2 is None and pelicula3 is None and pelicula4 is not None and pelicula5 is not None:
        mensaje = pelicula4 + ", " + pelicula5
    
    if pelicula1 is not None and pelicula2 is not None and pelicula3 is not None and pelicula4 is None and pelicula5 is None:
        mensaje = pelicula1 + ", " + pelicula2 + ", " + pelicula3
    
    if pelicula1 is not None and pelicula2 is not None and pelicula3 is None and pelicula4 is not None and pelicula5 is None:
        mensaje = pelicula1 + ", " + pelicula2 + ", " + pelicula4
    
    if pelicula1 is not None and pelicula2 is not None and pelicula3 is None and pelicula4 is None and pelicula5 is not None:
        mensaje = pelicula1 + ", " + pelicula2 + ", " + pelicula5
        
    if pelicula1 is not None and pelicula2 is None and pelicula3 is not None and pelicula4 is not None and pelicula5 is None:
        mensaje = pelicula1 + ", " + pelicula3 + ", " + pelicula4
        
    if pelicula1 is not None and pelicula2 is None and pelicula3 is not None and pelicula4 is None and pelicula5 is not None:
        mensaje = pelicula1 + ", " + pelicula3 + ", " + pelicula5
        
    if pelicula1 is not None and pelicula2 is None and pelicula3 is None and pelicula4 is not None and pelicula5 is not None:
        mensaje = pelicula1 + ", " + pelicula4 + ", " + pelicula5
        
    if pelicula1 is None and pelicula2 is not None and pelicula3 is not None and pelicula4 is not None and pelicula5 is None:
        mensaje = pelicula2 + ", " + pelicula3 + ", " + pelicula4
        
    if pelicula1 is None and pelicula2 is not None and pelicula3 is not None and pelicula4 is None and pelicula5 is not None:
        mensaje = pelicula2 + ", " + pelicula3 + ", " + pelicula5
        
    if pelicula1 is None and pelicula2 is not None and pelicula3 is None and pelicula4 is not None and pelicula5 is not None:
        mensaje = pelicula2 + ", " + pelicula4 + ", " + pelicula5
        
    if pelicula1 is None and pelicula2 is None and pelicula3 is not None and pelicula4 is not None and pelicula5 is not None:
        mensaje = pelicula3 + ", " + pelicula4 + ", " + pelicula5

    if pelicula1 is not None and pelicula2 is not None and pelicula3 is not None and pelicula4 is not None and pelicula5 is None:
        mensaje = pelicula1 + ", " + pelicula2 + ", " + pelicula3 + ", " + pelicula4
    
    if pelicula1 is not None and pelicula2 is not None and pelicula3 is not None and pelicula4 is None and pelicula5 is not None:
        mensaje = pelicula1 + ", " + pelicula2 + ", " + pelicula3 + ", " + pelicula5
    
    if pelicula1 is not None and pelicula2 is not None and pelicula3 is None and pelicula4 is not None and pelicula5 is not None:
        mensaje = pelicula1 + ", " + pelicula2 + ", " + pelicula4 + ", " + pelicula5
        
    if pelicula1 is not None and pelicula2 is None and pelicula3 is not None and pelicula4 is not None and pelicula5 is not None:
        mensaje = pelicula1 + ", " + pelicula3 + ", " + pelicula4 + ", " + pelicula5
        
    if pelicula1 is None and pelicula2 is not None and pelicula3 is not None and pelicula4 is not None and pelicula5 is not None:
        mensaje = pelicula2 + ", " + pelicula3 + ", " + pelicula4 + ", " + pelicula5
    
    if pelicula1 is not None and pelicula2 is not None and pelicula3 is not None and pelicula4 is not None and pelicula5 is not None:
        mensaje = pelicula1 + ", " + pelicula2 + ", " + pelicula3 + ", " + pelicula4 + ", " + pelicula5
        
    return mensaje

def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:
    """Indica cuantas peliculas de clasificación '18+' hay entre los diccionarios recibidos.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        int: Numero de peliculas con clasificacion '18+'
    """
    
    contador = 0
    
    clasificacion_pelicula_1 = p1["clasificacion"]
    clasificacion_pelicula_2 = p2["clasificacion"]
    clasificacion_pelicula_3 = p3["clasificacion"]
    clasificacion_pelicula_4 = p4["clasificacion"]
    clasificacion_pelicula_5 = p5["clasificacion"]
    
    if clasificacion_pelicula_1 == "18+":
        contador +=1
    if clasificacion_pelicula_2 == "18+":
        contador +=1
    if clasificacion_pelicula_3 == "18+":
        contador +=1
    if clasificacion_pelicula_4 == "18+":
        contador +=1
    if clasificacion_pelicula_5 == "18+":
        contador +=1
        
    return contador

def reagendar_pelicula(peli:dict, nueva_hora: int, nuevo_dia: str, 
                       control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)-> bool: 
    """Verifica si es posible reagendar la pelicula que entra por parametro. Para esto verifica
       si la nueva hora y el nuevo dia no entran en conflicto con ninguna otra pelicula, 
       y en caso de que el usuario haya pedido control horario verifica que se cumplan 
       las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula a reagendar
        nueva_hora (int): Nueva hora a la cual se quiere ver la pelicula
        nuevo_dia (str): Nuevo dia en el cual se quiere ver la pelicula
        control_horario (bool): Representa si el usuario quiere o no controlar
                                el horario de las peliculas.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        bool: True en caso de que se haya podido reagendar la pelicula, False de lo contrario.
    """
    
    hora_p1 = p1["hora"]
    hora_p2 = p2["hora"]
    hora_p3 = p3["hora"]
    hora_p4 = p4["hora"]
    hora_p5 = p5["hora"]
    
    dia_p1 = p1["dia"].lower()
    dia_p2 = p2["dia"].lower()
    dia_p3 = p3["dia"].lower()
    dia_p4 = p4["dia"].lower()
    dia_p5 = p5["dia"].lower()
    
    duracion_p1 = p1["duracion"]
    duracion_p2 = p2["duracion"]
    duracion_p3 = p3["duracion"]
    duracion_p4 = p4["duracion"]
    duracion_p5 = p5["duracion"]
    
    cambio = True
    
    if nuevo_dia == dia_p1 and hora_p1 <= nueva_hora <= hora_p1 + duracion_p1:
        cambio = False
    
    if nuevo_dia == dia_p2 and hora_p2 <= nueva_hora <= hora_p2 + duracion_p2:
        cambio = False
        
    if nuevo_dia == dia_p3 and hora_p3 <= nueva_hora <= hora_p3 + duracion_p3:
        cambio = False
        
    if nuevo_dia == dia_p4 and hora_p4 <= nueva_hora <= hora_p4 + duracion_p4:
        cambio = False
        
    if nuevo_dia == dia_p5 and hora_p5 <= nueva_hora <= hora_p5 + duracion_p5:
        cambio = False
    
    if cambio == True:
        peli["hora"] = nueva_hora
        peli["dia"] = nuevo_dia.capitalize()
    
    return cambio
    
def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool)-> bool:
    """Verifica si es posible invitar a la persona cuya edad entra por parametro a ver la 
       pelicula que entra igualmente por parametro. 
       Para esto verifica el cumplimiento de las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula que se desea ver con el invitado
        edad_invitado (int): Edad del invitado con quien se desea ver la pelicula
        autorizacion_padres (bool): Indica si el invitado cuenta con la autorizacion de sus padres 
        para ver la pelicula
    Retorna:
        bool: True en caso de que se pueda invitar a la persona, False de lo contrario.
    """
    
    c = "18+"
    
    if 16 <= edad_invitado < 18:
        c = "16+"
    elif 13 <= edad_invitado < 13:
        c = "13+"
    elif 7 <= edad_invitado < 13:
        c = "7+" 
    elif peli["clasificacion"].find("Todos") != -1:
        c = "Todos"
    
# =============================================================================
#     print("oloala", c)
# =============================================================================
    
    se_puede_invitar = False
    
    if edad_invitado >= 18:
        se_puede_invitar = True
    
    if edad_invitado >= 15 and peli["genero"].find("Terror") != -1:
        se_puede_invitar = True
    
    if c == peli["clasificacion"]:
        se_puede_invitar = True    
    
    if c != peli["clasificacion"] and autorizacion_padres == True:
        se_puede_invitar = True

    if c != peli["clasificacion"] and peli["genero"].find("Documental") != -1 and autorizacion_padres == False:
        se_puede_invitar = True
    
    
    return se_puede_invitar