#Ejervicio 1
num=int(input("Ingrese un número positivo "))

if num>0:
    print(num, " x ", 1, " = ", num*1)
    print(num, " x ", 2, " = ", num*2)
    print(num, " x ", 3, " = ", num*3)
    print(num, " x ", 4, " = ", num*4)
    print(num, " x ", 5, " = ", num*5)
    print(num, " x ", 6, " = ", num*6)
    print(num, " x ", 7, " = ", num*7)
    print(num, " x ", 8, " = ", num*8)
    print(num, " x ", 9, " = ", num*9)
    print(num, " x ", 10, " = ", num*10)
else:
    print("El número no es positivo, no es posible la operatoria")
print("")
#Ejercicio 2
print("Ejercicio 2 \n")
print("Ingrese dos dígitos")
num1= int(input("Ingrese dígitos 1: ")) 
num2= int(input("Ingrese dígitos 2: ")) 

if num1>0 or num2>0:
    print(num1, " + ", num2, " = ", num1+num2)
else: 
    print("El número no es positivo, no es posible la operatoria")

print("")
#Ejercicio 3
print("Ejercicio 3 \n")

num3=int(input("Ingrese un número mayor a 1 y menor a 101: "))

if num3>1 and num3<101:
    if num3%2 == 0:
        print ("El número ", num3, " es par")
    else:
        print ("El número ", num3, " es impar")
else: 
    print("El número no es válido")