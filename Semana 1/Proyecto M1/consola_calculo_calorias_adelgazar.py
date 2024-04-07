# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 22:32:14 2021

@author: HP
"""

import calculadora_indices as calc

def ejecutar_consumo_calorias_recomendado_para_adelgazar(peso: float) -> None:
    altura = float(input("\n\t\tIngrese su altura en centímetros (cm): "))
    edad = int(input("\n\t\tIngrese su edad en años: "))
    valor_genero = float(input("\n\t\tIngrese el valor de el parametro valor_genero. En caso de ser hombre introduzca el valor de 5 y en caso de ser mujer de -161: "))
    rango_de_calorias = calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)
    
    print("\n\t\t", rango_de_calorias, "\n")
    
def iniciar_aplicacion() -> None:
    peso = float(input("\n\t\tIntroduzca su peso en kilogramos (kg): "))
    ejecutar_consumo_calorias_recomendado_para_adelgazar(peso)
    
iniciar_aplicacion()