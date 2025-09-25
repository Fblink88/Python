
#Registro de usuario
print("")
usuario1=None
contrasena1=None
usuario2=None
contrasena2=None
usuario3=None
contrasena3=None
usuarios=[]
contrasenas=[]
numeros=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
import time
import getpass
while True:
    try:
        print("*-*-*-*-Menú-*-*-*-*")
        print("1. Iniciar sesión")
        print("2. Registrar usuario")
        print("3. Salir\n")
        opc1=int(input("Ingrese opción: "))
        if opc1==1:
            if usuarios!=[]:
                user=input("Ingrese nombre de usuario: ")
                if user in usuarios:
                    passw=getpass.getpass("Ingrese contraseña: ")
                    if passw in contrasenas:
                        while True:
                            try:
                                print("*-*-*-Sesión iniciada-*-*-*")
                                print("1. Realizar llamada")
                                print("2. Enviar correo electrónico")
                                print("3. Cerrar Sesión\n")
                                opc2=int(input("Ingrese opción: "))
                                if opc2==1:
                                    while True:
                                        numTel=input("Ingrese número telefónico\n(Recuerde que debe iniciar en 9\n y debe contener 9 dígitos):\n EJ: 987654321\n")
                                        if numTel.isnumeric():
                                            if numTel[0]=="9":
                                                if len(numTel)==9:
                                                    time.sleep(1)
                                                    print("Llamada realizada")
                                                    break
                                                else:
                                                    print("Recuerde que el número debe contener 9 dígitos")
                                                    break
                                            else:
                                                print("Recuerde que el número debe comenzar por 9")
                                                break
                                        else:
                                            print("Ingrese solo números")
                                        break
                                elif opc2==2:
                                    while True:
                                        correo=input("Ingrese correo electrónico al cual enviará mensaje: ")
                                        for i in correo:
                                            if "@" in correo:
                                                mensaje=input("Ingrese el mensaje: \n")
                                                time.sleep(1)
                                                print("Mensaje enviado")
                                                break
                                            else:
                                                print("Correo electrónico inválido")
                                                print("Recuerde que debe ser como el ejemplo: juan123@correo.com")
                                                break
                                        break
                                    
                                elif opc2==3:
                                    print("Cerrando sesión")
                                    time.sleep(1)
                                    print("Hasta pronto")
                                    break
                                else:
                                    print("Opción inválida")
                            except ValueError as error:
                                print("¡Error! ", error)

                    else: 
                        print("Contraseña incorrecta")
                else:
                    print("Usuario inválido")
            else:
                print("No existen usuario registrados")
        elif opc1==2:
            if usuario1==None:
                usuario1=input("Registre nombre de usuario: ")
                contrasena1=input("Registre constraseña: ")
                usuarios.append(usuario1)
                contrasenas.append(contrasena1)
                print("Registro usuario exitoso\n")
            elif usuario2==None:
                usuario2=input("Registre nombre de usuario: ")
                contrasena2=input("Registre constraseña: ")
                usuarios.append(usuario2)
                contrasenas.append(contrasena2)
                print("Registro usuario exitoso\n")
            elif usuario3==None:
                usuario3=input("Registre nombre de usuario: ")
                contrasena3=input("Registre constraseña: ")
                usuarios.append(usuario3)
                contrasenas.append(contrasena3)
                print("Registro usuario exitoso\n")
            else:
                print("Ya no quedan cupos para nuevos registros")
                while True:
                    modificar=input("¿Desea modificar algún usuario? (S/N): ").upper()
                    if modificar=="S":
                        print("Usuarios: ")
                        print(f"1. {usuario1}")
                        print(f"2. {usuario2}")
                        print(f"3. {usuario3}")
                        opc3=int(input("Ingrese opción para modificar usuario: "))
                        if opc3 == 1:
                            modificar1=input("Ingrese contraseña de usuario de quien desea modificar los datos: ")
                            if modificar1==contrasena1:
                                usuario1=input("Registre nuevo nombre de usuario: ")
                                contrasena1=input("Registre nueva constraseña: ")
                                usuarios.append(usuario1)
                                contrasenas.append(contrasena1)
                                print("Modificación de usuario exitosa")
                            else: 
                                print("Contraseña incorrecta")
                                print("No es posible modificar usuario")
                        elif opc3 == 2:
                            modificar2=input("Ingrese contraseña de usuario de quien desea modificar los datos: ")
                            if modificar2==contrasena2:
                                usuario2=input("Registre nuevo nombre de usuario: ")
                                contrasena2=input("Registre nueva constraseña: ")
                                usuarios.append(usuario2)
                                contrasenas.append(contrasena2)
                                print("Modificación de usuario exitosa")
                            else: 
                                print("Contraseña incorrecta")
                                print("No es posible modificar usuario")
                        elif opc3 == 3:
                            modificar3=input("Ingrese contraseña de usuario de quien desea modificar los datos: ")
                            if modificar3==contrasena3:
                                usuario3=input("Registre nuevo nombre de usuario: ")
                                contrasena3=input("Registre nueva constraseña: ")
                                usuarios.append(usuario3)
                                contrasenas.append(contrasena3)
                                print("Modificación de usuario exitosa")
                            else: 
                                print("Contraseña incorrecta")

                    elif modificar=="N":
                        print("Volviendo al menú")
                        break
                    else: 
                        print("opción no válida")
        elif opc1==3:
            print("Hasta pronto")
            break

        else:
            print("Opción inválida")

    except ValueError as error:                        
        print("¡Error! ", error)