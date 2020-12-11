# Escribe un programa que lea (entrada por teclado) el nombre y los dos apellidos de una persona
#  (en tres cadenas de caracteres diferentes), los pase como parámetros a una función, y ésta debe
#   unirlos y devolver una única cadena. La cadena final la imprimirá el programa por pantalla.
def nombreCompleto(a,b,c):
    junto= a+b+c
    return junto



nombre=input("Introduce nombre: ")
apelllido1=input("Introduce primer apellido: ")
apellido2=input("Introduce segundo apellido: ")
print(nombreCompleto(nombre,apelllido1,apellido2))