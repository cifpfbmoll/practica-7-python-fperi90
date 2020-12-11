# Escribe un programa que pida una frase (entrada por teclado), y pase la frase como parámetro a una 
# función que debe eliminar los espacios en blanco (compactar la frase). El programa principal imprimirá 
# por pantalla el resultado final
def elimina_espacios(nueva):
    x=nueva.replace(" ","")
    return x

frase=input("Introduce una frase, le vamos a quitar los espacios en blanco: ")
print(elimina_espacios(frase))




