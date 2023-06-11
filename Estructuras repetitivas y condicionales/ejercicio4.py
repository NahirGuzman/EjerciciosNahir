#Leer 10 números y mostrar solamente los números positivos, y su sumatoria.
x= 1

while x<=15:
    n= int(input(f"Ingrese un número {x}:"))
    if n>0:
        print (f"El número {x} es un número positivo")
    x +=1
  