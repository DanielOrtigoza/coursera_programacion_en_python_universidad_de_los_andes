# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 21:35:03 2021

@author: HP
"""

def calcular_IMC(peso: float, altura: float) -> float:
    """
    Calcula el indice de masa corporal (IMC) de una persona.

    Parameters
    ----------
    peso : float
        Peso de la persona en kilogramos (kg).
    altura : float
        Altura de la persona en metros (m).

    Returns
    -------
    float
        Índice de masa corporal de la persona.

    """

    return peso / (altura ** 2)

def calcular_porcentaje_grasa(peso: float, altura: float, edad: int, valor_genero: float) -> float:
    """
    Calcula el porcentaje de grasa corporal (% GC) de una persona.

    Parameters
    ----------
    peso : float
        Peso de la persona en kilogramos (kg).
    altura : float
        Altura de la persona en metros (m).
    edad : int
        Edad de la persona en años.
    valor_genero : float
        Valor que varía según el género de la persona: en caso de ser masculino
        debe ser 10.8 y en caso de ser femenino ser 0.

    Returns
    -------
    float
        El porcentaje de grasa que tiene la persona.

    """

    return (1.2 * calcular_IMC(peso, altura)) + (0.23 * edad) - 5.4 - valor_genero

def calcular_calorias_en_reposo(peso: float, altura: float, edad: int, valor_genero: int)-> float:
    """
    Calcula la cantidad de calorías que una persona quema estando en reposo,
    esto es su tasa metabólica basal (TMB).

    Parameters
    ----------
    peso : float
        Peso de la persona en kilogramos (kg).
    altura : float
        Altura de la persona en centímetros (cm).
    edad : int
        Edad de la persona en años.
    valor_genero : int
        Valor que varía según el género de la persona: en caso de ser masculino
        debe ser 5 y en caso de ser femenino debe ser -161.

    Returns
    -------
    float
        La cantidad de calorías que la persona quema en reposo

    """

    return (10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero

def calcular_calorias_en_actividad(peso: float, altura: float, edad: int, valor_genero: float, valor_actividad: float)-> float:
    """
    Calcula la cantidad de calorías que una persona quema al ralizar algún tipo
    de actividad física, esto es, su tasa metabólica basal según actividad física.

    Parameters
    ----------
    peso : float
        Peso de la persona en kilogramos (kg).
    altura : float
        Altura de la persona en centímetros (cm).
    edad : int
        Edad de la persona en años.
    valor_genero : float
        Valor que varía según el género de la persona: en caso de ser masculino
        debe ser 5 y en caso de ser femenino debe ser -161.
    valor_actividad : float
        Valor que depende de la actividad física semanal:
            - 1.2: poco o ningún actividad
            - 1.375: ejercicio ligero (1 a 3 días a la semana)
            - 1.55: ejercicio moderado (3 a 5 días a la semana)
            - 1.725: deportista (6 a 7 días a la seman)
            - 1.9: atleta (entrenamientos en la mañana y en la tarde)  

    Returns
    -------
    float
        La cantidad de calorías que una persona quema, al realizar algún tipo de
        actividad física semanalmente.

    """

    return calcular_calorias_en_reposo(peso, altura, edad, valor_genero) * valor_actividad

def consumo_calorias_recomendado_para_adelgazar(peso: float, altura: float, edad: int, valor_genero: float)-> str:
    """
    Calcula el rango de calorías recomendado, que debe consumir una persona
    diariamente en caso de que desee adelgazar.

    Parameters
    ----------
    peso : float
        Peso de la persona en kilogramos (kg).
    altura : float
        Altura de la persona en centímetros (cm).
    edad : int
        Edad de la persona en años.
    valor_genero : float
        Valor que varía según el género de la persona: en caso de ser masculino
        debe ser 5 y en caso de ser femenino debe ser -161.

    Returns
    -------
    str
        Una cadena indicando el rango de calorías que una persona debe consumir
        si desea adelgazar . El formato de la cadena debe ser : "Para adelgazar
        es recomendado que consumas entre: XXX y ZZZ calorías al día."
        Siendo XXX el rango inferior y ZZZ el rango superior.
    """
    
    inferior = str(round(calcular_calorias_en_reposo(peso, altura, edad, valor_genero) * 0.80, 2))
    superior = str(round(calcular_calorias_en_reposo(peso, altura, edad, valor_genero) * 0.85, 2))
    return "Para adelgazar es recomendado que consumas entre: " + inferior + " y " + superior + " calorías al día."