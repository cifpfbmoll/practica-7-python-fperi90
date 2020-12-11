# Escribir un programa que lea una frase, y pase ésta como parámetro a una función que debe contar el número de palabras que contiene. 
# Debe imprimir el programa principal el resultado. Asumir que cada palabra está separada por un solo blanco:
# Asumir que cada palabra está separada por un solo blanco.
# No se sabe cómo están separadas las palabras. Pueden estar separadas por más de un blanco o por signos de puntuación.

def contar_palabras(prueba):
    lista=prueba.split()
    return len(lista)
 
frase=str(input("Introduce una frase, vamos a mirar cuantas palabras tiene: "))
print(contar_palabras(frase))