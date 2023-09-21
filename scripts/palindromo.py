"""
Un palíndromo, también llamado palíndroma o palindroma, es una palabra o frase que se lee 
igual en un sentido que en otro (por ejemplo; Ana, Anna, Otto). Si se trata de números en 
lugar de letras, se llama capicúa.
Juanito, que trabaja en bienestar, necesita saber si una frase-palabra es Palíndroma, o un
número es capicúa.
Dado una cadena Input, el programa debe imprimir si es PALINDROMO o no.
"""

def is_palindrome(string):
    invert_string = string[::-1]
    return string == invert_string


def main():
    input_string = input("Ingresa una palabra:")

    while not input_string.strip():
        print("No has ingresado nada, por favor ingresa una palabra")
        input_string = input("Ingresa una palabra:")

    input_string = input_string.lower().strip()
    if is_palindrome(input_string):
        print(input_string + " Es palindroma")
    else:
        print(input_string + " No es palindroma")

main()