
# for --> para

#for i in range(3): #El range con un solo dato establece solo el stop
                   #El range con tres datos establece (star,stop,step)
                   #El range con dos datos establece el setp como defecto 1
#    print("Hola Mundo")


num1=int(input("Ingrese un número: "))

for i in range(1,11):
    print(f"{num1} x {i} = ", num1*i)