agua=600
azucar=1200
aceite=1500
arroz=1250
fideos=790
bebida=1780
chocolate=2500
panMolde=1340
producto=0
total=0
desc=0
print("Lista de compras")
print("1. Agua")
print("2. Azucar")
print("3. Aceite")
print("4. Arroz")
print("5. Fideos")
print("6. Bebida")
print("7. Chocolate")
print("8. Pan de molde")
try:
    while producto<8:
        producto+=1
        comprar=input(f" Producto {producto}: ¿Desea agregarlo al carro? (s/n): ").upper()
        if comprar=="S":
            if producto==1:
                cantidad=int(input("Ingrese cantidad: "))
                total=total+(agua*cantidad)
            elif producto==2:
                cantidad=int(input("Ingrese cantidad: "))
                total=total+(azucar*cantidad)
            elif producto==3:
                cantidad=int(input("Ingrese cantidad: "))
                total=total+(aceite*cantidad)
            elif producto==4:
                cantidad=int(input("Ingrese cantidad: "))
                total=total+(arroz*cantidad)
            elif producto==5:
                cantidad=int(input("Ingrese cantidad: "))
                total=total+(fideos*cantidad)
            elif producto==6:
                cantidad=int(input("Ingrese cantidad: "))
                total=total+(bebida*cantidad)
            elif producto==7:
                cantidad=int(input("Ingrese cantidad: "))
                total=total+(chocolate*cantidad)
            elif producto==8:
                cantidad=int(input("Ingrese cantidad: "))
                total=total+(panMolde*cantidad)
        elif comprar=="N":
            total
        else:
            print("Ingrese una opción válida")
            producto-=1
except ValueError:
    print("Error: Ingrese una opción válida")
try:
    while True:
        preferencial=input("¿Es usted cliente preferencial?(s/n): ").upper()
        if preferencial=="S":
            desc=total*0.25
            break
        elif preferencial=="N":
            break
        else:
            print("Ingrese una opción válida")        
except ValueError:
    print("Error: Ingrese una opción válida")

print("Subtotal:    $",total )
print("Descuento:   $",int(desc) )
total=total-desc
print("TOTAL:       $", int(total))

while True:
    try:
        pagar=int(input("Ingrese con cuanto dinero paga: $"))
        if pagar>=total:
            pagar=pagar-total
            print("Su vuelto es de: $", int(pagar))
            break
        else: 
            total=total-pagar
            print("Dinero insuficiente. Le faltan: $", int(total))
    except ValueError:
        print("Error: Ingrese una opción válida")