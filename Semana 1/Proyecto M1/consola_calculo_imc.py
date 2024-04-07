# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 22:31:59 2021

@author: HP
"""

import calculadora_indices as calc

def ejecutar_convertir_IMC(peso: float) -> None:
    altura = float(input("\n\t\tIntroduzca su altura en metros (m): "))                        
    IMC = calc.calcular_IMC(peso, altura)
    print("\n\t\tPara un peso de", peso, "kg y una altura de", altura,
          "m, el indice de masa corporal es de", round(IMC, 2), "\n")
    
def iniciar_aplicacion() -> None:
    peso = float(input("\n\t\tIntroduzca su peso en kilogramos (kg): "))
    ejecutar_convertir_IMC(peso)
    
iniciar_aplicacion()
