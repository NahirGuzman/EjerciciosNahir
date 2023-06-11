
#Ingresar las edades y el sexo de 15 personas y determinar cuántas son mujeres, cuántos varones, cuántos mayores de edad y cuántos menores de edad.

Mujeres= 0
Hombres= 0
MayoresEdad= 0
MenoresEdad= 0
for i in range(15):
    Edad= int(input("Ingrese la edad:"))
    Sexo= input("Ingrese el sexo de la persona (M/F):")
    if Sexo== "M":
        Hombres += 1
    elif Sexo=="F":
        Mujeres += 1
    else :
        print ("El sexo ingresado no es válido")

    if Edad>18:
        MayoresEdad += 1
    else:
        MenoresEdad += 1
    
print ("Mujeres:", Mujeres)
print ("Hombres:", Hombres)
print ("Mayores de edad:", MayoresEdad)
print ("Menores de edad:", MenoresEdad)

