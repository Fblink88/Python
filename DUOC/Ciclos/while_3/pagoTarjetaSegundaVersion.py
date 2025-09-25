#Segunda versión pago tarjeta
#Con saldo total de 200.000
saldo=100000
deuda=100000
import time
while True:
    try:
        print("\n     Menú    ")
        print("-------------")
        print("1. Pago tarjeta de crédito")
        print("2. Simulación de compras")
        print("3. Salir")
        opc1=int(input("Ingrese nº de opción: "))
        if opc1==1:
            while True:
                try:
                    print("\nCupo total:          $", saldo+deuda)
                    print("Saldo disponible:    $", saldo)
                    print("Su deuda es de:      $", deuda)
                    print("\nRealizar pago: ")
                    print("1. Pago total deuda: $", deuda)
                    print("2. Pago parcial")
                    print("3. Volver")
                    opc2=int(input("Ingrese nº de opción: "))
                    if opc2==1:
                        print("Realizando pago")
                        saldo+=deuda
                        deuda-=deuda
                        time.sleep(1)
                        print("Pago realizado")
                        break
                    elif opc2==2:
                        montoPagar=int(input("Ingrese monto a pagar: $"))
                        if montoPagar>0:
                            if montoPagar<deuda:
                                print("Realizando pago")
                                saldo+=montoPagar
                                deuda-=montoPagar
                                time.sleep(1)
                                print("Pago realizado")
                                break
                            else:
                                print("El monto a pagar no puede ser mayor a su deuda")
                        else:
                            print("Ingrese un monto mayor a 0")
                    elif opc2==3:
                        break
                    else:
                        print("Ingrese una opción válida")
                except ValueError:
                    print("Ingrese solo números")
        elif opc1==2:
            cantCompras=int(input("Ingrese la cantidad de comprar que desea realizar: "))
            for i in range(cantCompras):
                try:
                    compra=int(input(f"Ingrese el monto de compra {i+1}: "))
                    if compra<=saldo:
                        deuda+=compra
                        saldo-=compra
                        print("Compra realizada")
                    else:
                        print("Compra rechazada")
                        print("La compra no puede ser mayor al saldo disponible")
                except ValueError:
                    i-=1
                    print("Ingrese solo números")
        elif opc1==3:
            print(" Finalizando sesión")
            time.sleep(1)
            print("Hasta pronto")
        else:
            print("Ingrese una opción válida")    
    except ValueError:
        print("Ingrese solo números")