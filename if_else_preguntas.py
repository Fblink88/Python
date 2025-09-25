
print("Contesta la siguiente pregunta")
print("Dependiendo de tu respuesta será tu puntaje")
print("*******************************************")

print("¿Cuál de los siguientes animales vive en el mar")
print("Perro")
print("Cocodrilo")
print("Conejo")
print("Tiburón")
puntmayor=1
puntmedio=0.5
puntbajo=0

respuesta=input("Escriba su respuesta ")
respuesta=respuesta.upper().replace("Ó","O")

if respuesta=="TIBURON":
    print ("Respuesta correcta")
    print ("Tu puntaje es: ", puntmayor)
else:
    if respuesta=="COCODRILO":
        print ("Respuesta correcta")
        print ("Tu puntaje es: ", puntmedio)
    else:
        if respuesta=="CONEJO":
            print ("Respuesta incorrecta")
            print ("Tu puntaje es: ", puntbajo)
        else:
            if respuesta=="PERRO":
                    print ("Respuesta incorrecta")
                    print ("Tu puntaje es: ", puntbajo)
