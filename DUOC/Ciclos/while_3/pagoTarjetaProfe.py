#Solución profe
# El profesor cambia ejercicio y especifica que existe 
# un saldo de 100 y una deuda de 100. 
# Por lo que al pagar quedaría un saldo disponible de 200

deuda=100000
saldo=100000

while True:
    try:
        print("     Menu        ")
        print("*****************")
        print("1. Pago tarjeta de crédito")
        print("2. Simulación de compra")
        print("3. Salir\n")

        opcion=int(input("Ingrese su opción: "))
        print("")
        if opcion==1:
            print("Paga")
            while True:
                try:
                    print("Su saldo es: $", saldo)
                    print("Su deuda es: $", deuda)
                    montoPago=int(input("Ingrese el monto a pagar: "))

                    if montoPago<0:
                        print("El monto debe ser mayor a cero\n")
                    else:
                        if montoPago>deuda:
                            print("Pago excede deuda\n")
                        else:
                            deuda = deuda - montoPago
                            print("Usted pago: $", montoPago, "\n")
                            saldo = saldo + montoPago
                            break

                except:
                    print("Ingrese el monto válido a pagar")
        else:
            if opcion==2:
                print("Compra ")
                cantidadComprar=int(input("Ingrese cantidad de compras: "))
                for i in range(cantidadComprar):
                    print("Compra ", (i+1))
                    try:
                        montoCompra=int(input("Ingrese monto de compra: "))
                        if montoCompra <=0:
                            print("El monto de compra debe ser mayor a cero\n")
                        else:
                            if saldo>=montoCompra:
                                deuda=deuda+montoCompra
                                saldo=saldo-montoCompra
                                print("Ud compró un monto de $", montoCompra, "\n")
                            else: 
                                print("Saldo insuficiente\n")
                    except ValueError:
                        print("Debe ingresar un valor numérico para comprar\n")
            else:
                if opcion==3:
                    print("Saliendo\n")
                    break
                else:
                    print("Ingrese una opción válida")
    except ValueError:
        print("Ingrese una opción válida del 1 al 3\n")
