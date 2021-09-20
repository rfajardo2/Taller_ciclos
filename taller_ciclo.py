# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 08:31:02 2021

@author: Desarrollo
"""
""" 
El departamento de Seguridad de Transito de Barranquilla, desea saber de
los n autos que entrar a la ciudad, cuantos entran con calcomanía de cada
color. Conociendo el último digito de la placa de cada automóvil se puede
determinar el color de la calcomanía utilizando la siguiente relación:
DIGITO COLOR
1 o 2 Amarilla
3 o 4 Rosa
5 o 6 Roja
7 u 8 Verde
9 o 0 Azul 
"""
 

cont_amarilla = 0
cont_rosa = 0
cont_roja = 0
cont_verde = 0
cont_azul = 0
nautos = int(input('Digite la cantidad de autos que ingresaron a la ciudad: '))
for i in range(1,nautos + 1):
    dplaca = int(input('Digite el ultimo digito de la placa del vehiculo:'))
    if dplaca == 1 or dplaca == 2:
        cont_amarilla =+ 1
    elif dplaca == 3 or dplaca == 4:
        cont_rosa =+1
    elif dplaca == 5 or dplaca == 6:
        cont_roja =+1
    elif dplaca == 7 or dplaca == 8:
        cont_verde =+1            
    elif dplaca == 9 or  0:
        cont_azul =+1
print(f'La cantidad de autos con calcomania Amarilla es: {cont_amarilla}')
print(f'La cantidad de autos con calcomania Rosa es: {cont_rosa}')        
print(f'La cantidad de autos con calcomania Roja es: {cont_roja}')
print(f'La cantidad de autos con calcomania Verde es: {cont_verde}')
print(f'La cantidad de autos con calcomania Azul es: {cont_azul}')
