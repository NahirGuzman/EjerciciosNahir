#Realice un programa que lea dos números y diga cuál es el mayor
print ("Ingrese el primer número:")
número1=int(input())
print ("Ingrese el segundo número")
número2=int(input())
if número1>número2:
    print (número1, "es mayor que", número2)
else:
    print (número2, "es mayor que", número1)