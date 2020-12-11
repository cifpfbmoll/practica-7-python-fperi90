# Escribe un programa que le pida al usuario si quiere calcular si un número es primo con for o con while, por tanto, 
# habrá dos funciones que se caracterizan por hacer ese mismo cálculo de una manera (con for y sin breaks), o de otra 
# (con while). Ambas funciones devolverá true (si es primo) o false (si no es primo). El programa principal informará 
# del resultado. Además, como mejora puedes calcular el tiempo que tarda en encontrar la solución de una manera u otra.
#  Comentario: aprovecha el código que tienes ya creado.

def primo_con_while(pwh):
    inicio=1
    divisor=0
    while inicio<=numero and divisor <3:
    #al tenerl la posibilidad de poder poner una condicion en el bucle, no necesito recorrer necesariamente todos los elementos
    #hasta llegar al numero , solo evaluar si tiene mas de 2 divisores.
        if numero%inicio==0:
            print(inicio)
            divisor+=1
        inicio+=1
    if divisor!=2:
        print("El numero no es primo")
    elif divisor==2:
        print("El numero es primo")


numero=int(input("Introduce un numero, evaluaremos si es primo de dos maneras: "))
primo_con_while(numero)
primo_con_for(numero)


