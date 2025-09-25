
nombres=[]
continuar="SI"
while continuar=="SI":
    nombre=input(f"Ingrese nombre: ").upper()
    nombres.append(nombre)
    continuar=input("¿Desea ingresar otro nombre? (Si/No): ").upper()

nombreCorto=nombres[0]
for i in nombres:
    if len(i)<len(nombreCorto):
        nombreCorto=i
nombres.remove(nombreCorto)
print(nombres)

