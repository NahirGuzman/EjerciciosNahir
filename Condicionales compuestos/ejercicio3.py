#Realice un programa que lea tres números, muestre cuál es el mayor y determine si es par o impar
Número1= int(input("Introduce el primer número:"))
Número2= int(input("Introduce el segundo número:"))
Número3= int(input("Introduce el tercer número:"))

if Número1>Número2 and Número1>Número3:
    Mayor= Número1
elif Número2>Número1 and Número2>Número3:
    Mayor= Número2
else:
    Mayor= Número3
if Mayor%2==0:
    print ("El número mayor es",Mayor,"y es par")
else:
    print ("El número mayor es",Mayor,"y es impar")