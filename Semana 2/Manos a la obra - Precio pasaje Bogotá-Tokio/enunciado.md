# Ejercicio

La persona que vende pasajes aéreos en la compañía de turismo la libertad pierde mucho tiempo calculando el precio de los pasajes. Esto se debe a que el precio del pasaje depende de una tarifa básica, la temporada, la compañía aérea, la edad del pasajero y si este es estudiante o no. Usted deb hacer un programa que ayude a calcular el precio de un pasaje Bogotá-Tokio, teniendo en cuenta que:

  - La compañía ALAS incrementa el valor de sus pasajes en un 30 % en alta temporada mientras que la compañía VOLAR lo incrementa en solo 20 %
  - Ambas compañías descuentan el 50 % si el pasajero es menor de edad, ademas la compañía VOLAR tiene un recargo de $ 100,000.00 para los pasajeros mayores a 60 años para cubrir el seguro de vida
  - Los estudiantes que viajan por ALAS y que no son menores de edad, tienen un descuento del 10 % en temporada baja
  - La tarifa básica Bogotá-Tokio reglamentaria es de 5 millones de pesos

Entradas
  - compañia(string, puede ser ALAS o VOLAR)
  - edad (entero)
  - si es temporada alta (boolean, si es TRUE es temporada alta y FALSE de lo contrario)
  - si es estudiante (boolean, TRUE si es estudiante y FALSE de lo contrario)

Salidas
  - precio del pasaje (entero)