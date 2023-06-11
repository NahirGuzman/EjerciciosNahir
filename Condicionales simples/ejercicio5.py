#. Realice un programa que cambie pesos a dólares. Mejórelo, añadiendo el cambio de dólares a pesos y que sea el usuario quién decida qué tipo de cambio quiere, si de dólares a pesos o viceversa.

print ('Ingrese "pesos a dólares" o "dólares a pesos" dependiendo la operación que quiera hacer')
Cambio=input()
Cantidad= int(input("ingesar la cantidad de dinero a convertir"))
if Cambio=="pesos a dólares":
    convertir= Cantidad/500 
    print ("Sus", Cantidad,"equivalen a", convertir,"dólares" )
else:
    convertir= Cantidad/500 
    print ("Sus", Cantidad,"equivalen a", convertir,"dólares" )


