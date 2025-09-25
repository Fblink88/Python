
#Sistema Automatizado de Luces
patio=False
sala=False
pasillo=False
jardin=False
while True:
    print("")
    print("Menú de Sistema de Automatización de Luces")
    print("******************************************")
    print("1. Encender o Apagar luces Patio")
    print("2. Encender o Apagar luces Sala")
    print("3. Encender o Apagar luces Pasillo")
    print("4. Encender o Apagar luces Jardín")
    print("5. Encender Todo")
    print("6. Apagar Todo")
    print("7. Salir del sistema\n")

    opc=int(input("Ingrese una de las opciones: \n"))
    try:
        if opc==1:
            patio=not patio
            if patio==True:
                print("Encendiendo luces Patio")
            elif patio==False:
                print("Apagando luces Patio")
        elif opc==2:
            sala=not sala
            if sala==True:
                print("Encendiendo luces Sala")
            elif sala==False:
                print("Apagando luces Sala")
        elif opc==3:
            pasillo=not pasillo
            if pasillo==True:
                print("Encendiendo luces Pasillo")
            elif pasillo==False:
                print("Apagando luces Pasillo")
        elif opc==4:
            jardin=not jardin
            if jardin==True:
                print("Encendiendo luces Jardín")
            elif jardin==False:
                print("Apagando luces Jardín")
        elif opc==5:
            patio=True
            sala=True
            pasillo=True
            jardin=True
            print ("Encendiendo todas las luces")
        elif opc==6:
            patio=False
            sala=False
            pasillo=False
            jardin=False
            print ("Apagando todas las luces")
        elif opc==7:
            print("Saliendo del sistema")
            import time
            time.sleep(1)
            print("Hasta pronto")
            break
        else:
            print("Ingrese una opción válida")
    except: 
        print("Ingrese un valor numérico")
