#Realice un programa que lea 4 números y diga cuántos son pares y cuantos impares y devuelva la sumatoria de los pares.

Numero1= int(input("Introduce el primer número:"))
Numero2= int(input("Introduce el segundo número:"))
Numero3= int(input("Introduce el tercer número:"))
Numero4= int(input("Introduce el cuarto número:"))
Pares= 0
Impares= 0
Sumapares= 0
if Numero1%2==0:
    Pares+=1
    Sumapares+=Numero1
else:
    Impares+=1
if Numero2%2==0:
    Pares += 1
    Sumapares+=Numero2
else:
    Impares+=1
if Numero3%2==0:
    Pares+=1
    Sumapares+=Numero3
else:
    Impares+=1
if Numero4%2==0:
    Pares+=1
    Sumapares+=Numero4
else:
    Impares+=1
print ("Hay", Pares,"números pares y", Impares,"números impares")
print ("La sumatoria de los números pares es", Sumapares)