
#Ejercicio 1 tabla multiplicar

num1=int(input("Ingrese un número del 1 al 10 para mostrar su tabla de multiplicar\n"))
try:
    if num1>0 and num1<11:
        for i in range(1,11):
            multi=num1*i
            print(num1, " x ", i, " = ", multi )
    else:
        print("Ingrese un número según lo solicitado")
except ValueError:
    print("Ingrese un dato válido")