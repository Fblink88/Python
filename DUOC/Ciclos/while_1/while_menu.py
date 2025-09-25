print("")
#Repetir
while True:
    print("     Menu     ")
    print("**************")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")

    try:
        opc=int(input("Ingrese su opción: "))
        if opc==1:
            print("Esta es la opción 1")
        elif opc==2:
            print("Esta es la opción 2")
        elif opc==3:
            print("Saliendo")
            break
        else:
            print("Opción no válida")
    except:    
        print("Ingrese solo números")

totalIngresos=0
cantPasajes=0
valorPasaje=0
numPasaje=0
while True:
    try:
        cantPasajes = int(input("Ingrese la cantidad de pasajes: "))
    except:
        print("Ingrese valor numérico")
