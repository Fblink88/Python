#Errores
#try:
#   bloque de código
#except:
#    Se maneja el error
#else:
#   Que no pasa nada
#finally:
#   este bloque siempre se ejecuta

while True:
    try:
        num=int(input("Ingrese un número: "))
        break
    except:
        print("Debes ingresar solo números")

#Se puede hacer así también

while True:
    try:
        num=int(input("Ingrese un número: "))
    except:
        print("Debes ingresar solo números")
    else:
        print("Estamos bien")
        break
    finally:
        print("Buenísima")


