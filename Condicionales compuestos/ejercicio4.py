#. Confeccione un programa que pida un número del 1 al 7 y diga el día de la semana correspondiente.
Día= int(input("Ingresa un número:"))
if Día==1:
    print ("Lunes")
elif Día==2:
    print ("Martes")
elif Día==3:
    print ("Miércoles")
elif Día==4:
    print ("Jueves")
elif Día==5:
    print ("Viernes")
elif Día==6:
    print ("Sábado")
elif Día==7:
    print ("Domingo")
else:
    print ("Este día no es válido")