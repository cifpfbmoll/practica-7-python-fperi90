# Escribe un programa que pida un texto por pantalla, 
# este texto lo pase como parámetro a un procedimiento, y
#  éste lo imprima primero todo en minúsculas y luego todo en mayúsculas.
def cambiarTexto(texto):
    print (texto.lower())
    print (texto.upper())




texto = str(input("Introduce un texto, lo vamos a cambiar: "))
cambiarTexto(texto)