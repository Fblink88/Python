#Ejercicio Sushi
pikachu=0
otaku=0
pulpo=0
anguila=0
precioPikachu=4500
precioOtaku=5000
precioPulpo=5200
precioAnguila=4800
codDescuento="SOYOTAKU"
porcentajeDesc=0.9
descuento=None
entrada=True
print("\n*__*__*__*__*__*__*__*__*__*__*")
print("     Menu venta de Sushi ")
print("*--*--*--*--*--*--*--*--*--*--*")
while entrada==True:
    try:
        print("Selecciones el roll a elección:")
        print("1. Pikachu Roll              $4500")
        print("2. Otaku Roll                $5000")
        print("3. Pulpo Venenoso Roll       $5200")
        print("4. Anguila Eléctrica Roll    $4800\n")
        while True:
            opc2=input("Desea agregar roll al pedido: (S/N)").upper()
            if opc2=="S":
                opc1=int(input("Ingrese el Roll que desea ordenar: "))
                if opc1==1:
                    pikachu+=1
                    print("Orden de Pikachu Roll agregada correctamente\n")
                elif opc1==2:
                    otaku+=1
                    print("Orden de Otaku Roll agregada correctamente\n")
                elif opc1==3:
                    pulpo+=1
                    print("Orden de Pulpo Venenoso Roll agregada correctamente\n")
                elif opc1==4:
                    anguila+=1
                    print("Orden de Anguila Eléctrica Roll agregada correctamente\n")
                else:
                    print("Opción no válida\n")
            elif opc2=="N":
                while True:
                    try:
                        pregDescuento=input("¿Posee código de descuento?(S/N)").upper()
                        if pregDescuento=="S":
                            while True:
                                try:
                                    descuento=input("Ingrese código de descuento si posee alguno: ").upper()
                                    if descuento==codDescuento:
                                        totalPikachu=precioPikachu*pikachu*porcentajeDesc
                                        totalOtaku=precioOtaku*otaku*porcentajeDesc
                                        totalPulpo=precioPulpo*pulpo*porcentajeDesc
                                        totalAnguila=precioAnguila*anguila*porcentajeDesc
                                        totalcantRoll=pikachu+otaku+pulpo+anguila
                                        totalValorSinDescuento=(precioPikachu*pikachu)+(precioPulpo*pulpo)+(precioOtaku*otaku)+(precioAnguila*anguila)
                                        totalValorRollFinal=totalOtaku+totalPikachu+totalAnguila+totalPulpo
                                        totalDescuento=totalValorSinDescuento-totalValorRollFinal
                                        print("\n**************************************")
                                        print("          Total del pedido")
                                        print("**************************************")
                                        print("Tipo de Roll         Cantidad   Precio")
                                        print(f"Pikachu:                {pikachu}       ${int(totalPikachu)}")
                                        print(f"Otaku:                  {otaku}       ${int(totalOtaku)}")
                                        print(f"Pulpo venenoso:         {pulpo}       ${int(totalPulpo)}")
                                        print(f"Anguila eléctrica:      {anguila}       ${int(totalAnguila)}")
                                        print("**************************************")
                                        print(f"Total:                  {totalcantRoll}       ${int(totalValorSinDescuento)}")
                                        print(f"Descuento:           {descuento}   ${int(totalDescuento)}")
                                        print(f"Total:                          ${int(totalValorRollFinal)}")
                                        print(f"")
                                        break
                                    elif descuento=="X":
                                        break
                                    else:
                                        print("Código de descuento no válido\n")
                                        print("*Ingrese X si desea volver al menú*")
                                except ValueError as error:
                                    print("Error: Ingrese solo números")
        
                        elif pregDescuento=="N":
                            totalPikachu=precioPikachu*pikachu
                            totalOtaku=precioOtaku*otaku
                            totalPulpo=precioPulpo*pulpo
                            totalAnguila=precioAnguila*anguila
                            totalcantRoll=pikachu+otaku+pulpo+anguila
                            totalValorSinDescuento=(precioPikachu*pikachu)+(precioPulpo*pulpo)+(precioOtaku*otaku)+(precioAnguila*anguila)
                            totalValorRollFinal=totalOtaku+totalPikachu+totalAnguila+totalPulpo
                            totalDescuento=totalValorSinDescuento-totalValorRollFinal
                            print("\n**************************************")
                            print("          Total del pedido")
                            print("**************************************")
                            print("Tipo de Roll         Cantidad   Precio")
                            print(f"Pikachu:                {pikachu}       ${int(totalPikachu)}")
                            print(f"Otaku:                  {otaku}       ${int(totalOtaku)}")
                            print(f"Pulpo venenoso:         {pulpo}       ${int(totalPulpo)}")
                            print(f"Anguila eléctrica:      {anguila}       ${int(totalAnguila)}")
                            print("**************************************")
                            print(f"Total:                  {totalcantRoll}       ${int(totalValorSinDescuento)}")
                            print(f"Descuento:             {descuento}     ${int(totalDescuento)}")
                            print(f"Total:                          ${int(totalValorRollFinal)}")
                            print(f"")
                            break
                        else:   
                            print("Opción no válida")
                        break
                    except ValueError as error:
                        print("Error: Ingrese solo números")
                          
                break
            else: 
                print("Opción no válida")

        while True:
            try:
                volver=input("¿Desea otro pedido?(S/N)").upper()
                if volver=="S":
                    print("1. Nuevo pedido")
                    print("2. Modificar pedido anterior")
                    nuevo=int(input("Ingrese nº de la opción: "))
                    if nuevo==1:
                        pikachu=0
                        otaku=0
                        pulpo=0
                        anguila=0
                        print("")
                        break
                    elif nuevo==2:
                        print("")
                        break
                    else:
                        print("Ingrese opción válida")

                elif volver=="N":
                    entrada=False
                    break
                else:
                    print("Ingrese opción válida")
            except ValueError as error:
                print("Error: Ingrese solo números")
    except ValueError as error:
        print("Error: Ingrese solo números")