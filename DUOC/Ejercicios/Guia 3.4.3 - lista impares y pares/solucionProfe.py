
def validar_lista_numeros():
    while True:
        try: 
            numeros = input("Ingrese lista de números separados por espacio: ").split() #Genera una lista e introduce los elementos separados por un espacio
            for i in range(len(numeros)):
                numeros[i]=int(numeros[i])
            return numeros
        except ValueError:
            print("Error: Ingrese solo números válidos enteros")

listaPares=[]
listaImpares=[]
datos= validar_lista_numeros()
for num in datos:
    if num % 2 == 0:
        listaPares.append(num)
    else:
        listaImpares.append(num)
    
print (datos)
print (listaImpares)
print (listaPares)