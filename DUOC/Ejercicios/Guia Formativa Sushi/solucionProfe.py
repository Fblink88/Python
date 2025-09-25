pikachu=4500
otaku=5000
pulpo=5200
anguila=4800
contarP=0
contarO=0
contarPul=0
contarA=0
total=0
desc=0
resp="s"
while resp == "s":
    while True:
        try:
            print("1. Pikachu Roll              $4500")
            print("2. Otaku Roll                $5000")
            print("3. Pulpo Venenoso Roll       $5200")
            print("4. Anguila Eléctrica Roll    $4800")
            print("5. Terminar pedido")

            opc1=int(input("Ingrese su opción: "))

            if opc1==1:
                contarP=contarP+1
                total= total + pikachu
            else:
                if opc1==2:
                    contarO=contarO+1
                    total=total+otaku
                else:
                    if opc1==3:
                        contarPul=contarPul+1
                        total=total+pulpo
                    else:
                        if opc1==4:
                            contarA=contarA+1
                            total=total+anguila
                        else:
                            if opc1==5:
                                break

        except ValueError:
            print("Ingrese opción válida")
    try:
        opcDesc=input("¿Tiene código de descuento?(s/n): ").lower()
        if opcDesc=="s":
            while True:
                codigo=input("Ingrese código de descuento: ").lower()
                if codigo=="soyotaku":
                    desc=total*0.1
                    break
                else:
                    print("Código no válido")
                    print("Si desea ingresar presionar ENTER o para salir ingresar X: ")
                    respX=input().lower()
                    if respX=="x":
                        break
    except ValueError:
            print("Ingrese opción válida")

    totalPagar=total-desc
    sumaCont=contarA+contarO+contarP+contarPul
    print("*************************************")
    print("Total productos: ", sumaCont)
    print("Pikachu Roll: ", contarP)
    print("Otaku Roll: ", contarO)
    print("Pulpo Venenoso Roll: ", contarPul)
    print("Anguila Eléctrica Roll: ", contarA)
    print("*************************************")
    print("Subtotal por pagar: $", total)
    print("Descuento por código: $",desc)
    print("TOTAL: $", totalPagar)

    resp = input("Desea volver a comprar (s/n): ").lower()
