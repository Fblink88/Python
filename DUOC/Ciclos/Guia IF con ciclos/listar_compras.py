productos = {
    "agua": 600,
    "azucar": 1200,
    "aceite": 1500,
    "arroz": 1250,
    "fideos": 790,
    "bebida": 1780,
    "chocolate": 2500,
    "panMolde": 1340
}
total = 0
print("Lista de compras")
try:
    for i, precio in productos.items():
        while True:
            comprar = input(f"- {i.capitalize()} ¿Desea agregar este producto al carro? (s/n): ").upper()
            if comprar == "S":
                total = total + precio
                break
            elif comprar == "N":
                break
            else:
                print("Ingrese una opción válida")
except ValueError:
    print("Error: Ingrese una opción válida")
try:
    while True:
        preferencial=input("¿Es usted un cliente preferencial? (s/n): ").upper()
        if preferencial=="S":
            total=total*0.75
            break
        elif preferencial=="N":
            break
        else:
            print("Ingrese una opción válida")
except ValueError:
    print("Error: Ingrese una opción válida")

print("El total de su compra es:", int(total))
