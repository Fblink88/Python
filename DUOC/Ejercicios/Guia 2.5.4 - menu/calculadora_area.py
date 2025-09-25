
#Calculadora geométrica
print("")
print("********Menu********")
print("1. Calcular Perímetro")
print("2. Calcular Área")
print("3. Salir\n")

while True:
    try:
        opc=int(input("Elija una opción"))
        if opc==1:
            print("Menu Perímetro")
            print("===============")
            print("Calcular círculo")
            print("Calcular rectángulo")
            print("Calcular cuadrado")
            print("Volver a menu principal")
            try:
                opc2=int(input("Elija una opción"))

                if opc2==1:
                    diametro=float(input(""))
                
        
            except ValueError as error:
                print("¡Error!: ", error)

            

    except ValueError as error:
        print("¡Error!: ", error)

    

