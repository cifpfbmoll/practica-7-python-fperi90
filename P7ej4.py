# Escribe un programa que pida una frase (entrada por teclado), y
# le pase como parámetro a una función dicha frase. La función debe sustituir
# todos los espacios en blanco de una frase por un asterisco, 
# y devolver el resultado para que el programa principal la imprima por pantalla.

def cambiaFrase(frase):
    nueva=frase.replace(" ","*")
    print (nueva)

frase=input("Introduce una frase, le vamos a cambiar los espacios por asteriscos: ")
cambiaFrase(frase)

# for i in range(len(frase)):
#     letra=frase[i]
#     if letra==" ":
#         print("*",end="")
#     else:
#         print (letra,end="")