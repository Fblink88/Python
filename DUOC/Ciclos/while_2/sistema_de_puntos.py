
#PuntosAcumulados
puntos = 100000
while True:

    print("1. Ver mis puntos")
    print("2. Gastar mis puntos")
    print("3. Salir")
    
    try:
        op=int(input("Seleccione una opción: "))
        if op > 0 and op <4:
            if op==1:
                print(f"Tiene un total de puntos de: {puntos}")
           
            elif op==2:
                print("Seleccione el producto a canjear")
                print("1.-  Gift Card de $10.000, valor de 10.000 puntos")
                print("2.-  Secadora de pelo, valor de: 25.000 puntos")
                print("3.-  Disco duro portátil, valor de: 30.000 puntos")
                continu = int(input("Seleccione la opción"))
                if continu==1:
                        if puntos>=10000:
                            puntos = puntos-10000
                            print(f"Canje exitoso, le quedan: ${puntos} puntos")
                        else:
                            print("\nNo quedan puntos suficientes\n")
                elif continu==2:
                        if puntos>=25000:
                            puntos = puntos-25000
                            print(f"Canje exitoso, le quedan: ${puntos} puntos")
                        else:
                            print("\nNo quedan puntos suficientes\n")
                elif continu==3:
                        if puntos>=30000:
                            puntos = puntos-30000
                            print(f"Canje exitoso, le quedan: ${puntos} puntos")
                        else:
                            print("\nNo quedan puntos suficientes\n")
            elif op==3:
                print("Adiós")
                break
    
    except:
          print("Opción no válida")







