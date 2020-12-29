# Escribe un programa que lea el nombre de una persona y un carácter (entrada por teclado),
# le pase estos datos a una función que comprobará si dicho carácter está en su nombre. 
# El resultado de dicha función lo imprimirá el programa principal por pantalla.

def busca_vocal(nombre,caracter):
    evalua=nombre.rfind(caracter)
    if evalua>=0:
        return ("si se encuentra en la palabra")
    elif evalua==(-1):
        return("no se encuentra en la palabra")
    
nombre=input("Introduce un nombre: ")
caracter=input("introduce una vocal: ")
valor=busca_vocal(nombre,caracter)
print(valor)

# nombre=input("Introduce un nombre ,vamos a comprobar si la letra esta edentro de el: ")
# caracter=input("Introduce la letra    ")
# evalua=nombre.rfind(caracter)
# print (evalua)

# contador=0
# for i in range(len(nombre)):
#     letra=nombre[i]
#     if letra==caracter:
#         contador+=1
# if contador>0:
#     print("La letra si se encuentra")
# elif contador==0:
#     print("La letra no se encuentra")