# Escribe un programa que lea (entrada por teclado) una frase,
#  y la pase como parámetro a un procedimiento, y éste debe mostrar 
#  la frase con un carácter en cada línea.
def caracterLinea(frase):
    indice=0
    for i in range(len(frase)):
        letra=frase[i]
        print (letra)



frase=input("Introduce una frase, la vamos a dividir en un caracter por linea: ")
caracterLinea(frase)
