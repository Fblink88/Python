usuarios=[]
contrasenas=[]
i=0
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
            if inicioUsuario in usuarios:
                if inicioContrasena in contrasenas:
                    if usuarios.index(inicioUsuario)==contrasenas.index(inicioContrasena):
                        print("Inicio de sesión exitoso")
                    else:
                        print("Usuario y contraseña no coinciden")
                else:
                    print("Contraseña inválida")
            else:    
                print("Usuario inválidos")
        elif opc1==2:
            print("Registro de usuario")
            usuario=input("Ingrese un nombre de usuario: ")
            contrasena=input("Ingrese una contraseña: ")
            usuarios.append(usuario)
            contrasenas.append(contrasena)
            print(usuarios)
            print(contrasenas)
        elif opc1==3:
            print("Eliminar usuario")
            usuarioEliminar=input("Ingrese usuario que desea eliminar: ")
            if usuarioEliminar in usuarios:
                contrasenaEliminar=input("Ingrese contraseña del usuario: ")
                if contrasenaEliminar in contrasenas:
                    if usuarios.index(usuarioEliminar)==contrasenas.index(contrasenaEliminar):
                        usuarios.remove(usuarioEliminar)
                        contrasenas.remove(contrasenaEliminar)
                        print("Usuario eliminado con éxito")
                        print(usuarios)
                        print(contrasenas)
                    else:
                        print("Usuario y contraseña no coinciden")
                else:
                    print("Contraseña inválida")
            else:    
                print("Usuario inválidos")
        elif opc1==4:
            break
        else:
            print("Ingrese una opción válida")    
        
    except ValueError:
        print ("Error: Ingrese una opción válida")
