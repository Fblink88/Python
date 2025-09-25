def validar_lista_numeros():
    for i in listaCompleta:
        if i == int:
            flag=True

flag=False
listaCompleta=[]
listaPares=[]
listaImpares=[]

while flag==False: 
    numerosUsuario=input("Ingresas números separados por un espacio (" ")")
    listaCompleta=numerosUsuario.split()
    for i in listaCompleta:
        i=int(i)
    print(listaCompleta)
    validar_lista_numeros()
    print(flag)


for i in listaCompleta:
    i = int(i)
    if i % 2 == 0:
        listaPares.append(i)
    else:
        listaImpares.append(i)
    

print (listaImpares)
print (listaPares)