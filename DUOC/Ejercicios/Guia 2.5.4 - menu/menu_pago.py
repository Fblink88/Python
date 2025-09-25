
#Sistema de pago página Dulce Capricho

while True:
    print("")
    print("             Menu             ")
    print("······························")
    print("1. Pago con tarjeta de crédito")
    print("2. Pago con Paypal")
    print("3. Pago por transferencia")
    print("4. Cancelar")#Es necesario?????
    print("5. Salir")
    try:
        opc=int(input("Ingrese opción: "))
        if opc==1:
            pago=int(input("Ingrese monto a pagar:          "))
            numTC=(input("Ingrese nº Tarjeta de crédito:  "))
            numTCAst=len(numTC)
            numTC=numTC[:4]
            nameTC=input("Ingrese nombre de Titular:      ")
            monthExp=input("Ingrese mes de vencimiento(nº): ")
            yearExp=input("Ingrese año de vencimiento:     ")
            print("\n Detalle de compra:")
            print("------------------------")
            print("Valor total de la compra:            ", pago)
            print("Número de tarjeta:                   ", numTC, (numTCAst-4)*"*")
            print("Nombre de Titular:                   ", nameTC)
            print("Fecha vencimiento:                   ", monthExp,"/",yearExp)
            print("")
            print("Hasta Pronto")
            break
        
        elif opc==2:
            pago=int(input("Ingrese monto a pagar:    "))
            usuario=input("Ingrese nombre de usuario:  ")
            import getpass
            contrasena=getpass.getpass("Ingrese contraseña:     ")
            print("\n Detalle de compra:")
            print("------------------------")
            print("Valor total de la compra:    ", pago)
            print("Usuario:         ", usuario)
            print("Contraseña:      ", "*"*len(contrasena))
            print("")
            print("Hasta Pronto")
            break

        elif opc==3:
            import random
            valorReferencia=random.randint(1000,9999)
            pago=int(input("Ingrese monto a pagar:    "))
            name=input("Ingrese nombre de quien transfiere: ")
            rut=input("Ingrese Rut de quien transfiere: ")
            email=input("Ingrese correo electrínico de quien transfiere:  ")
            print("")
            print("Transfiera a: ")
            print("---------------")
            print(" Nombre: Empresa Dulce Capricho \n", "Rut: 75.011.013-8\n", "Número cuenta corriente: 0187653649\n", "Banco: Banco Chile\n", "Correo: pago.transferencias@dulcecapricho.cl\n")
            enter=input("Pulse Enter luego de realizar transferencia")
            print("Validando transferencia")
            import time
            time.sleep(2)
            print("Transferencia realizada con éxito")
            print("\n Detalle de compra:")
            print("------------------------")
            print("Valor total de la compra:    ", pago)
            print("Código de referencia: ", "#",valorReferencia)
            print("Nombre de quien transfiere: ", name)
            print("Rut de quien transfiere: ", rut )
            print("Correo electrónico de quien transfiere: ", email)
            print("")
            print("Hasta Pronto")
            break
        elif opc==4:
            print("Cancelando operación")
            time.sleep(1)
            print("Hasta Pronto")
            break
        elif opc==5:
            print("")
            print("Hasta Pronto")
            break
        else:
            print("Opción no válida")

    except ValueError as error :
        print("¡Error!: ", error, "Ingrese dato según lo solicitado")