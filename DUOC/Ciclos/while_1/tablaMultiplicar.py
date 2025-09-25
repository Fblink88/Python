num1=int(input("Ingrese un dígito para realizar tabla de multiplicar: "))
multi=0
while multi<10:
    multi=multi+1
    resultado=multi*num1
    print(f"{num1} x {multi} = {resultado}")