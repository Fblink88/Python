
#Esto son 2 dimensiones (Fila y columna)
matriz = [
    ["1","2","3"],
    [4,5,6]
]

print (matriz)

for elemento in matriz:
    print (elemento)

for fila in range(2):
    for columna in range(3):
        print(matriz[fila][columna])
    print()
#Esto es convención, usar "i" y "j" (fila y columna)
# for i in range(2):
#     for j in range(3):
#         print(matriz[i][j])
#     print()

for fila in matriz:
    for elemento in fila:
        print(elemento,end=" ")

#En 3 dimensiones (Capa(lado del cubo), Fila y Columna)

