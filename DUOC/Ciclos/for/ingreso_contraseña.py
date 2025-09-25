diccionario = {
    "hola":"perro"
}
usuario=input("Nombre: ")
contrasena=input("Contraseña: ")

diccionario [usuario]=contrasena

for usu, contra in diccionario.items():
    print(usu, ": ",contra)

perro = []

comentario1=input("Ingrese comentario: ")
perro.append(comentario1)
print(perro)
comentario2=input("Ingrese comentario: ")
perro.append(comentario2)
print(perro)

diccionario["Comentario"]=perro

for usu, contra in diccionario.items():
    print(usu, ": ",contra)

# rut=input("Ingrese rut: ")
# nombre=input("In")

i=0
num=input("nombre: ")