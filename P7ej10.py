# Escribe un programa que te pida una palabra o número, pase por parámetro estos datos a una función, 
# y ésta te diga si es o no palíndroma o capicúa. El programa principal imprimirá el resultado de la función:

def es_capicua(palabrain):
    if (palabrain)==(palabrain[::-1]):
        afirma=print("La palabra es capicua")
        return afirma
    else:
        niega=print("La palabra no es capicua")
        return niega
 

palabra=input("Introduce una palabra o un numero, vamos a ver si es capicua:  ")
contador=0
es_capicua(palabra)