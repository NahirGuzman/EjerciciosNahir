#Leer 15 números negativos y convertirlos a positivos e imprimir dichos números.
x = 1

while x<=15:
    n= int(input(f"Ingrese un número{x}:"))
    Resultado=abs(n)
    print ("Resultado:",n,"en positivo es", Resultado)
    x +=1
