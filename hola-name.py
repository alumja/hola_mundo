# -*- codung: utf-8 -*-
"""
Escribir script que pregunte el nombre del usuario en la consola y una número entero e imprima por pantalla
en líneas distintas el nombre de usuario tantas veces como el número introducido.

"""

name = (input("¿Cómo te llamas? "))
print(name + "\n")
n = int((input("Introduce un número entero: "))
if n >= 0:
    print((name + "\n") * int(n))
else:
    print("No funciona")