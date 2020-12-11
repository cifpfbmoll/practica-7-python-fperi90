# Escribe un programa que lea una frase (entrada por teclado), y la pase como parámetro a un procedimiento. 
# El procedimiento contará el número de vocales (de cada una) que aparecen, y lo imprimirá por pantalla.

def contar_vocales(fraseinterna):
    nuevaA=frase.count("a",0,len(fraseinterna))
    print(" a:",nuevaA,end="")
    nuevaE=frase.count("e",0,len(fraseinterna))
    print(" e:",nuevaE,end="")
    nuevaI=frase.count("i",0,len(fraseinterna))
    print(" i:",nuevaI,end="")
    nuevaO=frase.count("o",0,len(fraseinterna))
    print(" o:",nuevaO,end="")
    nuevaU=frase.count("u",0,len(fraseinterna))
    print(" u:",nuevaU,end="")

frase=str(input("Introduce una frase, le vamos a contar las vocales: "))
contar_vocales(frase)




# nuevaA=frase.count("a",0,len(frase))
# print(" a:",nuevaA,end="")
# nuevaE=frase.count("e",0,len(frase))
# print(" e:",nuevaE,end="")
# nuevaI=frase.count("i",0,len(frase))
# print(" i:",nuevaI,end="")
# nuevaO=frase.count("o",0,len(frase))
# print(" o:",nuevaO,end="")
# nuevaU=frase.count("u",0,len(frase))
# print(" u:",nuevaU,end="")



# contador=0
# for i in range(len(frase)):
#     letra=frase[i]
#     if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
#         contador+=1
# print (contador)