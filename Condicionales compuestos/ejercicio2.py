#. Realice un programa que le permita al usuario simular el pago ingresando el importe y la forma de pago: Contado (1): se aplica un descuento del 10% al importe. Tarjeta (2): se aplica un interés de 10%. Débito (3): se aplica un descuento del 5%. Mostrar el importe, el descuento o interés y el importe total.

Importe= float(input("Introduce el importe:"))
Formapago= int(input("Introduce la forma de pago (1:Contado, 2:Tarjeta, 3:Débito):"))

if Formapago==1:
    Descuento= Importe*0.1
    Total= Importe-Descuento
    print("Importe:",Importe)
    print("Descuento:",Descuento)
    print("Total a pagar:",Total)
elif Formapago==2:
    Interes=Importe*0.1
    Total= Importe+Interes
    print("Importe:",Importe)
    print("Interés:",Interes)
    print("Total a pagar:",Total)
elif Formapago==3:
    Descuento= Importe*0.05
    Total= Importe-Descuento
    print("Importe:",Importe)
    print("Descuento:", Descuento)
    print("Total a pagar:",Total)
