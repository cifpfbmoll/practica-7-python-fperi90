# Escribe un programa que pida dos palabras las pase como parámetro a un procedimiento y diga si riman o no.
# Si coinciden las tres últimas letras tiene que decir que riman.
# Si coinciden solo las dos últimas tiene que decir que riman un poco y si no, que no riman
def compara_palabras(palabra1,palabra2):
    if (palabra1[-3:]==palabra2[-3:]):
        print("Las palabras",palabra1," y ",palabra2,"riman")
        return 
    elif (palabra1[-2:]==palabra2[-2:]):
        print("Las palabras",palabra1," y ",palabra2,"riman poco")
        return 
    else:
        print("Las palabras",palabra1," y ",palabra2,"no riman")
        return 

palabra1=input("Dame una palabra: ")
palabra2=input("Dame otra palabra: ")
compara_palabras(palabra1,palabra2)


# palabra1=input("Dame una palabra")
# palabra2=input("Dame otra palabra")
# riman=palabra2.find(palabra1[-3:])
# rimanPoco=palabra2.find(palabra1[-2:])
# if riman==1:
#     print("Las palabras riman")
# elif rimanPoco==2:
#     print("Las palabras riman un poco")
# else:
#     print("Las palabras no riman")
# print(riman)
# print(rimanPoco)