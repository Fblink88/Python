nombres=[]
apellidos=[]

for i in range(3):
    i=i+1
    nombre=input(f"Ingrese nombre {i}: ").capitalize()
    apellido=input(f"Ingrese apellido {i}: ").capitalize()
    nombres.append(nombre)
    apellidos.append(apellido)
print (nombres)
print (apellidos)

for i in range(3):
    print(nombres[i], " ",apellidos[i])