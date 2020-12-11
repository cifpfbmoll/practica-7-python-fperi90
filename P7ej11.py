# Escribe un programa que te pida una frase, y pase la frase como parámetro a una función. 
# Ésta debe devolver si es palíndroma o no, y el programa principal escribirá el resultado por pantalla:
def es_capicua(auxiliar):
    frasein=auxiliar.replace(" ","",len(auxiliar))
    if (frasein)==(frasein[::-1]):
        afirma=str("La frase es capicua")
        return afirma
    else:
        niega=str("La frase no es capicua")
        return niega
 

frase=input("Introduce una frase, vamos a ver si es capicua:  ")
contador=0
print(es_capicua(frase))