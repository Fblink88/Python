# nombres=[]

# print("Ingrese 3 nombres distintos")
# for i in range(3):
#     i=i+1
#     nombre=input(f"Ingrese nombre {i}:")
#     nombres.append(nombre)

# nombres.sort(key=len)
# nombres.reverse()
# print(nombres[0], " es el nombre más largo")

#Esto lo cree yo
nombres=[]

print("Ingrese 3 nombres distintos")
for i in range(3):
    i=i+1
    nombre=input(f"Ingrese nombre {i}:")
    nombres.append(nombre)

if len(nombres[0]) > len(nombres[1]):
    if len(nombres[0])>len(nombres[2]):
        print(nombres[0], " es el nombre más largo")
    else:
        print(nombres[2], " es el nombre más largo")

else: 
    if len(nombres[1])>len(nombres[2]):
        print(nombres[1], " es el nombre más largo")
    else:
        print(nombres[2], " es el nombre más largo")

#Esto lo hizo el Fonchi

# nombres=[]

# print("Ingrese 3 nombres distintos")
# for i in range(3):
#     i=i+1
#     nombre=input(f"Ingrese nombre {i}:")
#     nombres.append(nombre)
# nombreLargo = nombres[0]
# for nombre in nombres:
#     if len(nombre)>len(nombreLargo):
#         nombreLargo=nombre
# print(f"El nombre más largo es {nombreLargo}")