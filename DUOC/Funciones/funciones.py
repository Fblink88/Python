
import defFunciones as fn

#Existen 4 tipos funciones
"""
Funciones sin argumentos y sin retorno
Funciones sin argumento y y con retorno
Funciones con argumentos y con retorno
Funciones con argumentos y sin retorno
"""

#Definir una función

# def saludo1 (): #Sin Argumento y sin retorno
#     print("Hola") 

# def saludoNombre(nombre):#Con argumento y sin retorno
#     print("Hola", nombre)

# def suma():#Sin argumento y con retorno
#     suma = 3+2
#     return suma

# def suma2(num1, num2):
#     suma = num1 + num2
#     return suma
#Llamando funciones 

fn.saludo1()#Llamado 1
fn.saludoNombre("Juaco")#Llamado 2
print(fn.suma())#Llamado 3
num1=int(input("Ingrese nº 1: "))
num2=int(input("Ingrese nº 2: "))
print(fn.suma2(num1,num2))


#Se debe agregar el método definido en la importación como en (fn)