# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 22:32:09 2021

@author: HP
"""

import calculadora_indices as calc

def ejecutar_calcular_porcentaje_grasa(peso: float) -> None:
    altura = float(input("\n\t\tIngrese su altura en metros (m): "))
    edad = int(input("\n\t\tIngrese su edad en años: "))
    valor_genero = float(input("\n\t\tIngrese el valor de el parametro valor_genero. En caso de ser hombre introduzca el valor de 10.8 y en caso de ser mujer de 0: "))
    porcentaje_GC = calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
    print("\n\t\tPara un peso de", peso, "kg, una altura de", altura,
          "m, una edad de", edad, "años y con un indice de valor genero de", valor_genero,
          "el porcentaje de grasa corporal es de", round(porcentaje_GC, 2), "%.\n")
    
def iniciar_aplicacion() -> None:
    peso = float(input("\n\t\tIntroduzca su peso en kilogramos (kg): "))
    ejecutar_calcular_porcentaje_grasa(peso)
    
iniciar_aplicacion()
