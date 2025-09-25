
liviano=1000
normal=2000
pesoLiviano=0
pesoNormal=0
cantLiviano=0
cantNormal=0

cantBultos=int(input("Ingrese la cantidad de bultos: "))

for i in range(cantBultos):
    pesoBulto=float(input("Ingrese el peso del bulto (kg): "))
    if pesoBulto>0 and pesoBulto<=10:
        if pesoBulto >0 and pesoBulto<=5:
            pesoLiviano=pesoLiviano+pesoBulto
            cantLiviano=cantLiviano+1
        elif pesoBulto>5 and pesoBulto<=10:
            pesoNormal=pesoNormal+pesoBulto
            cantNormal=cantNormal+1
    else:
        print("Peso no válido")
    

print("El valor a pagar es: ", round((pesoLiviano*liviano)+(pesoNormal*normal)))
print("La cantidad de bultos livianos es: ", cantLiviano)
print("La cantidad de bultos normal es: ", cantNormal)