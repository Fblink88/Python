##calcular edad
print("Calculo de edad")
añoActual = int(input("Ingrese año Actual: "))
añoNac = int(input("Ingrese año Nacimiento: "))
edad = añoActual - añoNac
print("Su edad es: ",edad," años app.")

##print("Probando GIT")

if edad >= 18:
    print ("Usted es mayor de edad")
else: 
    if edad > 0 and edad <= 4:
        print ("Usted es un bebe")
    else:
        if edad > 4 and edad <= 12:
            print ("Usted es un niño")
        else: 
            if edad>=13 and edad < 18:
                print ("Usted es un adolescente")


## Más adelante manejaremos elif que significa "si no si"
##if edad >= 18:
##    print ("Usted es mayor de edad")
##elif edad > 0 and edad <= 4:
##    print ("Usted es un bebe")        
##elif edad > 4 and edad <= 12:
##    print ("Usted es un niño")
##elif edad>=13 and edad < 18:
##    print ("Usted es un adolescente")