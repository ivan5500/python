"""
Mauricio le gustan mucho jugar con los numero, en especial los números primos, 
el tiene un gusto especial por el numero 3 y  5.

Escriba un código que imprima los números del 1 al 100, con la condición que si 
el numero a imprimir es múltiplo de 3 imprima la palabra “TIK”, si el numero es 
múltiplo de 5 imprima “TOK”, y si es múltiplo de ambos (3 y 5 ) imprima TIKTOK.
"""

sequence = range(1, 101)
for number in sequence:
    if number % 3 == 0 and number % 5 == 0:
        print("TIKTOK")
    elif number % 3 == 0:
        print("TIK")
    elif number % 5 == 0:
        print("TOK")
    else:
        print(number)