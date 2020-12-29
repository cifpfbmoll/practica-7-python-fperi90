# Escribe un programa que te pida una frase y una vocal (entrada por teclado),
# y pase estos datos como parámetro a una función que se encargará de cambiar 
# todas las vocales de la frase por la vocal seleccionada. Devolverá la función
#  la frase modificada, y el programa principal la imprimirá:

def nueva(frase,vocal):
    nueva=frase.replace("a",vocal).replace("e",vocal).replace("i",vocal).replace("o",vocal).replace("u",vocal)
    return nueva




frase=input("Introduce una frase, le vamos a cambiar las vocales: ")
vocal=input("Introduce la vocal: ")
print(nueva(frase,vocal))


# for i in range(len(frase)):
#     letra=frase[i]
#     if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
#         print(vocal,end="")
#     else:
#         print (letra,end="")