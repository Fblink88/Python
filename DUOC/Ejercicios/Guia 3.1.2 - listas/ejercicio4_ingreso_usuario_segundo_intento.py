usuarios=[]
usuario=[]
i=0
imprimir=0
while True:
    try:
        print("1. Inicio de sesión")
        print("2. Registrar usuario")
        print("3. Eliminar usuario")
        print("4. Salir")
        opc1=int(input("Ingrese la opción que desee: "))
        if opc1==1:
            print("Inicio de sesión")
            inicioUsuario=input("Nombre de usuario: ")
            inicioContrasena=input("Contraseña: ")
            if range(len(usuarios))==0:
                print("No existen usuarios registrados")
            else:
                for i in range(len(usuarios)):
                    if inicioUsuario in usuarios[i][0]:
                        if inicioContrasena in usuarios[i][1]:
                            print("Inicio de sesión exitoso")
                        else:
                            print("Contraseña no coincide con Usuario")
                    else:
                        print("Usuario no existe") 
        elif opc1==2:
            print("Registro de usuario")
            nombre=input("Ingrese un nombre de usuario: ")
            contrasena=input("Ingrese una contraseña: ")
            usuario=[nombre, contrasena]
            usuarios.append(usuario)
        elif opc1==3:
            print("Eliminar usuario")
            usuarioEliminar=input("Ingrese usuario que desea eliminar: ")
            for i in range(len(usuarios)):
                if usuarioEliminar in usuarios[i][0]:
                    contrasenaEliminar=input("Ingrese contraseña de usuario que desea eliminar: ")
                    if contrasenaEliminar in usuarios[i][1]:
                        usuarios[i].remove(usuarioEliminar)
                        usuarios[i].remove(contrasenaEliminar)
                        print("Inicio de sesión exitoso")
                    else:
                        print("Contraseña no coincide con Usuario")
                else:
                    print("Usuario no existe")
          
        elif opc1==4:
            break
        else:
            print("Ingrese una opción válida")    
        
    except ValueError:
        print ("Error: Ingrese una opción válida")
