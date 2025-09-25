usuario1={}
usuario2={}
usuario3={}

while True:
    usuario=input("nombre: ")
    contrasena=input("Contraseña: ")
    if usuario1=={}:
        usuario1[usuario]=contrasena
    elif usuario2=={}:
        usuario2[usuario]=contrasena
    elif usuario3=={}:
        usuario3[usuario]=contrasena
        break
    else:
        break

print("Usuario : Contraseña ")
for user, pasw in usuario1.items() :
    print (user, ": ", pasw)
for user, pasw in usuario2.items() :
    print (user, ": ", pasw)
for user, pasw in usuario3.items() :
    print (user, ": ", pasw)