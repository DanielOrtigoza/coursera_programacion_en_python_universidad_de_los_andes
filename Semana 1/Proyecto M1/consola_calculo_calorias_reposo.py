# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 22:32:11 2021

@author: HP
"""

import calculadora_indices as calc

def ejecutar_calcular_calorias_en_reposo(peso: float) -> None:
    altura = float(input("\n\t\tIngrese su altura en centímetros (cm): "))
    edad = int(input("\n\t\tIngrese su edad en años: "))
    valor_genero = float(input("\n\t\tIngrese el valor de el parametro valor_genero. En caso de ser hombre introduzca el valor de 5 y en caso de ser mujer de -161: "))
    
    tasa_metabolica_basal = calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    
    print("\n\t\tPara un peso de", peso, "kg, una altura de", altura,
          "cm, una edad de", edad, "años y con un indice de valor genero de", valor_genero,
          "la tasa metabólica basal (TMB) es de", round(tasa_metabolica_basal, 2), "cal.\n")
    
def iniciar_aplicacion() -> None:
    peso = float(input("\n\t\tIntroduzca su peso en kilogramos (kg): "))
    ejecutar_calcular_calorias_en_reposo(peso)
    
iniciar_aplicacion()
