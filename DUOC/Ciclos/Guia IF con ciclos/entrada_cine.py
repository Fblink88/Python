estreno=4800
normal=2900
palomitaP=2500
palomitaM=4500
palomitaG=7800
bebidaP=1000
bebidaM=1250
bebidaG=2000
total=0
descuento=0.7
i=1
print("\n*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")
print("*               CineDuoc              *")
print("*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*\n")
while True:
    try:
        duoc=input("¿Usted pertenece a Duoc(estudiante o funcionario)? (s/n): ").upper()
        if duoc=="S":
            duoc=True
            print("Pertenece a Duoc: ", duoc)
            break
        elif duoc=="N":
            duoc=False
            print("Pertenece a Duoc: ", duoc)
            break
        else:
            print("Ingresa opción válida")
    except ValueError:
        print("Error: Ingrese una opción válida")
while True:
    try: 
        print("¿Qué entradas desea?")
        print("1. Estreno: $", estreno)
        print("2. Normal: $", normal)
        entradas=int(input("Ingrese la opción que desee: "))
        if entradas==1:
            cantidad=int(input("Ingrese la cantidad de entradas que desea: "))
            if duoc==True:
                total=total+(estreno*cantidad*descuento)
            else:
                total=total+(estreno*cantidad)
            break
        elif entradas==2:
            cantidad=int(input("Ingrese la cantidad de entradas que desea: "))
            if duoc==True:
                total=total+(normal*cantidad*descuento)
            else:
                total=total+(estreno*cantidad)
            break
        else:
            print("Ingrese una opción válida")
    except ValueError:
        print("Error: Ingrese una opción válida")

while True:
    try:
        palomitas=input("¿Desea comprar palimitas?(s/n): "). upper()
        if palomitas=="S":
            cantP=int(input("Ingrese la cantidad que desea: "))
            for i in range(cantP):
                while True:
                    print("¿Qué tamaño desea?")
                    print("1. Pequeña: $", palomitaP)
                    print("2. Mediana: $", palomitaM)
                    print("3. Grande: $", palomitaG)
                    tamanoP=int(input("Ingrese su opción: "))
                    if tamanoP==1:
                        total=total+palomitaP
                        break
                    elif tamanoP==2:
                        total=total+palomitaM
                        break
                    elif tamanoP==3:
                        total=total+palomitaG
                        break
                    else:
                        print ("Ingrese una opción válida")
                        cantP=i-1
            break    
        elif palomitas=="N":
            break
        else:
            print("Ingrese opción válida")
    except ValueError:
        print("Error: Ingrese una opción válida")

while True:
    try:
        bebidas=input("¿Desea comprar bebidas?(s/n): "). upper()
        if bebidas=="S":
            cantB=int(input("Ingrese la cantidad que desea: "))
            for i in range(cantB):
                while True:
                    print("¿Qué tamaño desea?")
                    print("1. Pequeña: $", bebidaP)
                    print("2. Mediana: $", bebidaM)
                    print("3. Grande: $", bebidaG)
                    tamanoB=int(input("Ingrese su opción: "))
                    if tamanoB==1:
                        total=total+bebidaP
                        break
                    elif tamanoB==2:
                        total=total+bebidaM
                        break
                    elif tamanoB==3:
                        total=total+bebidaG
                        break
                    else:
                        print ("Ingrese una opción válida")
                        cantB=i-1
            break    
        elif bebidas=="N":
            break
        else:
            print("Ingrese opción válida")
    except ValueError:
        print("Error: Ingrese una opción válida")
while True:
    try:
        print("El total a pagar es: $", int(total))    
        pagar=int(input("Ingrese con cuanto dinero paga: $"))
        if pagar>=total:
            pagar=pagar-total
            print("Su vuelto es de: $", int(pagar))
            break
        else: 
            total=total-pagar
            print("Dinero insuficiente. Le faltan: $", int(total))
    except ValueError:
        print("Error: Ingrese una opción válida")