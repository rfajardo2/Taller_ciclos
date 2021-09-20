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
for i in range(1, nautos + 1):
    dplaca = int(input('Digite el ultimo digito de la placa del vehiculo:'))
    if dplaca == 1 or dplaca == 2:
        cont_amarilla = + 1
    elif dplaca == 3 or dplaca == 4:
        cont_rosa = + 1
    elif dplaca == 5 or dplaca == 6:
        cont_roja = + 1
    elif dplaca == 7 or dplaca == 8:
        cont_verde = + 1
    elif dplaca == 9 or 0:
        cont_azul = + 1
print(f'La cantidad de autos con calcomania Amarilla es: {cont_amarilla}')
print(f'La cantidad de autos con calcomania Rosa es: {cont_rosa}')
print(f'La cantidad de autos con calcomania Roja es: {cont_roja}')
print(f'La cantidad de autos con calcomania Verde es: {cont_verde}')
print(f'La cantidad de autos con calcomania Azul es: {cont_azul}')


# --------------------------------------------------------------

"""
Un ZoÃ³logo pretende determinar el porcentaje de animales que hay en las
siguiente categorias de edades: 0 a 1 aÃ±o, de mas de 1 aÃ±o y menos de 3 y
de 3 o mas aÃ±os. El zoolÃ³gico todavÃ­a no estÃ¡ seguro del animal que va
estudiar. Si se decide por elefantes solo tomarÃ¡ una muestra de 20 de ellos;
si se decide por jirafas, tomara 15 de muestras y si son chompancÃ©s tomarÃ¡
40.
"""

categoria1 = 0
categoria2 = 0
categoria3 = 0
print('1 = Elefantes')
print('2 = Jirafas')
print('3 = Chimpances')
p = int(input('Selecciona un numero del 1 al 3: '))

if p > 0:
    if p == 1:
        animal = 'Elefantes'
        total = 20
    elif p == 2:
        animal = 'Jirafas'
        total = 15
    elif p == 3:
        animal = 'Chimpances'
        total = 40
else:
    print('Digita un numero dentro del rango permitido del 1 al 3')

for i in range(1, total + 1):
    edad = int(input('Ingresa la edad por favor: '))
    if edad >= 0 and edad <= 1:
        categoria1 = + 1
    elif edad > 1 and edad < 3:
        categoria2 = + 1
    elif edad >= 3:
        categoria3 = + 1
calculo = float((categoria1 / total)) * 100
if p == 1:
    print(f'Porcentaje de edad de: {animal}')
    print(f'{calculo} porcentaje de 0 1 year')
elif p == 2:
    print(f'Porcentaje de edad de: {animal}')
    print(f'{calculo} porcentaje de mas de 1 year y menos de 3')
elif p == 3:
    print(f'Porcentaje de edad de: {animal}')
    print(f'{calculo} porcentaje de 3 o mas year')


# --------------------------------------------------------------------------

"""
Una empresa se requiere calcular el salario semanal de cada uno de los n
obreros que laboran en ella. El salario se obtiene de la siguiente forma:
a. Si el obrero trabaja 40 horas o menos se le paga $20 por hora
b. Si trabaja mas de 40 horas se le paga $20 por cada una de
lasprimeras 40 horas y $25 por cada hora extra
 """
salario = 0
x = 1
horas = 0
hextras = 0
num_obreros = int(input('Por favor digite el numero de obreros que aboran en la empresa: '))

if num_obreros >= 1:
    for x in range(1, num_obreros + 1):
        horas = int(input('Por favor digite el numero de horas trabajadas:'))

        if horas >= 1 and horas <= 40:
            salario = float(horas * 20)
        else:
            hextras = horas - 40
            salario = 40 * 20 + (hextras * 25)
        x = + 1
        print(f'El salario del trabajador {x} es:  {salario}')


# --------------------------------------------------------------------
"""
Calcular el promedio de edades de hombres, mujeres y de todo un grupo
de alumnos.
"""
x = 1
suma = 0
sh = 0
sf = 0
totalal = int(input('Por favor ingrese el total de alumnos: '))

for x in range(1, totalal + 1):
    ed = int(input('Ingresa tu edad: '))
    sx = input('Por favor ingresa tu sexo(M o F): ')
    suma = suma + ed
    if sx == 'M' or sx == 'm':
        sh =  suma+ed
    elif sx == 'F' or sx == 'f':
        sf == suma + ed
    x=+1
print(f'El promedio de edades de todo el grupo es de:', suma/totalal)
print(f'El promedio de edades de Hombres es de:', sh/totalal)
print(f'El promedio de edades de Mujeres es de:', sf/totalal)


# --------------------------------------------------------------------


"""Encontrar el menor valor de un conjunto de n números dados"""

num = int(input("Por favor digita el total de numeros a calcular: "))
x = 1
for x in range(1, num + 1):

    n = int(input("Por favor digita un numero: "))
    if x == 1:
        nm = n
    elif n < nm:
        nm = n
    x = + 1
print(f'El numero menor es: {nm}')
















