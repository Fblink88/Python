
print("")
saldo=500000

while True:
    print("     Menu cajero     ")
    print("---------------------")
    print("1. Ver Mi Saldo")
    print("2. Retirar dinero")
    print("3. Salir")

    try:
        opc=int(input("Ingrese opción: "))
        if opc>0 and opc<4:
            if opc==1:
                print(f"Tiene un saldo de: {saldo}")
                print("----------------------------")
                print("1. volver atrás")
                print("2. salir")
                volver=int(input("Ingrese opción: "))
                if volver==1:
                    print("")
                elif volver==2:
                    print("Cierre de sesión exitoso")
                    break
            elif opc==2:
                    retiro=int(input("¿Cuánto desea retirar?: "))
                    if retiro<=saldo:
                        print("Retiro exitoso")
                        saldo=saldo-retiro
                    else:
                        print("Saldo insuficiente")
            elif opc==3:
                    print("Cierre de sesión exitoso")
                    break
    except:
        print ("Ingrese respuesta válida")