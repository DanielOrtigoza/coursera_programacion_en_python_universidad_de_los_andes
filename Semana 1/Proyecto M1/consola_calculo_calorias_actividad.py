# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 22:32:13 2021

@author: HP
"""

import calculadora_indices as calc

def ejecutar_calcular_calorias_en_actividad(peso: float) -> None:
    altura = float(input("\n\t\tIngrese su altura en centímetros (cm): "))
    edad = int(input("\n\t\tIngrese su edad en años: "))
    valor_genero = float(input("\n\t\tIngrese el valor de el parametro valor_genero. En caso de ser hombre introduzca el valor de 5 y en caso de ser mujer de -161: "))
    valor_actividad = float(input("\n\t\tIngrese el valor de el parametro valor_actividad. Este valor correcponde a la cantidad de actividad física que realiza por semana siendo esta de:\n\t\t\t1.2: poco o ningún actividad\n\t\t\t1.375: ejercicio ligero (1 a 3 días a la semana)\n\t\t\t1.55: ejercicio moderado (3 a 5 días a la semana)\n\t\t\t1.725: deportista (6 a 7 días a la seman)\n\t\t\t1.9: atleta (entrenamientos en la mañana y en la tarde)\n\t\tIngrese el valor que mejor se adapte a su caso: "))
    consumo_de_calorias_diarias = calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)
    
    print("\n\t\tPara un peso de", peso, "kg, una altura de", altura,
          "cm, una edad de", edad, "años, con un indice de valor genero de", valor_genero,
          "y un indice de actividad de", valor_actividad, "el consumo de calorias diarias es de",
          round(consumo_de_calorias_diarias, 2), "cal.\n")
    
def iniciar_aplicacion() -> None:
    peso = float(input("\n\t\tIntroduzca su peso en kilogramos (kg): "))
    ejecutar_calcular_calorias_en_actividad(peso)
    
iniciar_aplicacion()