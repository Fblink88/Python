totalIngresos=0
totalPasaje=0
numPasaje=0
while True:
    try:
        cantPasajes = int(input("Ingrese la cantidad de pasajes: "))
        break
    except:
        print("Ingrese valor numérico")
for i in range(cantPasajes):
    while True:
        try:
            #numPasaje=numPasaje+1
            valorPasaje=int(input(f"Ingrese el valor del pasaje #{i+1}: "))
            totalPasaje=totalPasaje+valorPasaje
            break
        except ValueError as error:
            print(f"¡Error!. Ingrese un valor válido")
            #numPasaje=numPasaje-1

print(f"La cantidad de pasaje es {cantPasajes} por un costo total de {totalPasaje}")