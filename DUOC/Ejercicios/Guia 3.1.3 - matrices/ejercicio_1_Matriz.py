
arreglo = []
lista=[]

for i in range(3):
    numeros=input("Ingrese 4 nros separados por un espacio: ")
    lista=numeros.split()
    for i in lista:
        i=int(i)
    arreglo.append(lista)
print("La matriz es (directo en un print): ")
print(arreglo)

print("La matriz es (Print en un for): ")
for i in arreglo:
    print (i)