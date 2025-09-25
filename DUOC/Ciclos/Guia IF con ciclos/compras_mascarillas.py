#Mascarillas

mascarilla=500
envioSuperior=0
envioMismaComuna=1000
envioComunaAledana=2000
envioOtraComuna=3000
while True:
    try:
        cantMasc=int(input("Ingrese la cantidad de mascarilla que desea comprar: "))
        total=mascarilla*cantMasc
        if total>=15000:
            print("El total a pagar para las ",cantMasc, " mascarillas es: $", total )
            print("El despacho tendrá un valor de : $", envioSuperior)
            break
        elif total<15000 and total>0:
            while True:
                try:
                    print("Ingrese lugar de despacho para calcular envío")
                    print("1. Misma comuna")
                    print("2. Comuna aledaña")
                    print("3. Otra comuna")
                    destino=int(input("Ingrese su opción: "))
                    if destino==1:
                        print("El total a pagar para las ",cantMasc, " mascarillas es: $", total )
                        print("El despacho tendrá un valor de : $", envioMismaComuna)
                        break
                    elif destino==2:
                        print("El total a pagar para las ",cantMasc, " mascarillas es: $", total )
                        print("El despacho tendrá un valor de : $", envioComunaAledana)
                        break
                    elif destino==3:
                        print("El total a pagar para las ",cantMasc, " mascarillas es: $", total )
                        print("El despacho tendrá un valor de : $", envioOtraComuna)
                        break
                    else:
                        print("Opción no válida")
                except ValueError:
                    print("Ingrese una opción válida")
        break
            
    except ValueError:
        print("Ingrese una opción válida")