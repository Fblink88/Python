
#Pago Tarjetas
deuda=100000
salir=1
numCompras=0
totalCompras=0
compras=1
while salir==1:
    try:
        print("\n     Tarjeta de crédito      ")
        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        print("1. Pago de Tarjeta de crédito")
        print("2. Compras")
        print("3. Salir")
        opc=int(input("Ingrese nº de opcíon: "))
        if opc==1:
            if deuda>0:
                print(f"\n Su saldo actual es de: $-{deuda}")
                print("¿Desea Pagar?")
                print(f"1. Pagar ${deuda}")
                print("2. Pagar otro monto")
                pagar=int(input("Ingrese nº de opcíon: "))
                if pagar==1:
                    deuda=deuda-deuda
                    print("Pago exitoso. Su nuevo saldo es: $", deuda, "\n")
                    print("¿Volver al menú?")
                    print("1. Volver")
                    print("2. Salir")
                    while True:
                        volver=int(input("Ingrese nº de opcíon: "))
                        if volver==1:
                            print("")
                            break
                        elif volver==2:
                            print("Finalizando programa")
                            import time
                            time.sleep(1)
                            print("Hasta pronto")
                            salir=33
                            break
                        else:
                            print("Opción no válida")
                elif pagar==2:
                        while True:
                            pagarMonto=int(input("Ingrese monto a pagar: "))
                            if pagarMonto>=0 and pagarMonto<=deuda:
                                deuda=deuda-pagarMonto
                                if deuda==0:
                                    print("Pago exitoso. Su nuevo saldo es: $", deuda)
                                else:
                                    print("Pago exitoso. Su nuevo saldo es: $-", deuda)
                                print("¿Volver al menú?")
                                print("1. Volver")
                                print("2. Salir")
                                while True:
                                    volver=int(input("Ingrese nº de opcíon: "))
                                    if volver==1:
                                        print("")
                                        break
                                    elif volver==2:
                                        print("Finalizando programa")
                                        import time
                                        time.sleep(1)
                                        print("Hasta pronto")
                                        salir=33
                                        break
                                    else:
                                        print("Opción no válida")
                                break
                            elif pagarMonto<0:
                                print("Monto debe ser igual o superior a 0")
                            elif pagarMonto>deuda:
                                print("El monto a pagar debe ser menor a su deuda de: $-", deuda)
            else:
                print("No posee deuda que pagar")
        elif opc==2:
            cantCompras=int(input("Ingrese cantidad de compras a realizar: "))
            while True:
                if cantCompras>0:
                    for i in range(cantCompras):
                        numCompras=numCompras+1
                        compras=int(input(f"Ingrese monto de comprar {numCompras} "))
                        totalCompras=totalCompras+compras
                else:
                    print("No se realizó ninguna compra")
                if numCompras==1:
                    print(f"El valor total a pagar por su compra es: ", totalCompras)
                elif numCompras>1:
                    print(f"El valor total a pagar por sus {cantCompras} compras es: ", totalCompras)
                deuda=deuda+totalCompras
                numCompras=0
                break

        if opc==3:
            print("Finalizando programa")
            time.sleep(1)
            print("Hasta pronto")
            salir=33
        else:
            print("Ingrese opción válida")
    except ValueError:
        print ("¡Error!: Ingresar solo valores numéricos")

