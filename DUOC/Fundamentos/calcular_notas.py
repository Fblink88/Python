
print("Ingrese 3 notas para calcular el promedio")

nota1=float(input("Ingrese primera nota "))
nota2=float(input("Ingrese segunda nota "))
nota3=float(input("Ingrese tercera nota "))
promedio=(nota1+nota2+nota3)/3
print("Tu promedio es: ", promedio)

if promedio>= 4:
    print("Aprobaste")
else:
    print("Reprobado")