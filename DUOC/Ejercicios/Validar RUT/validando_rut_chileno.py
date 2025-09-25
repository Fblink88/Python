# Autor: Fabián Basaes
# Descripción: Verificador de RUT chileno
# Fecha: 06-06-2024


#SOLUCIÓN VERIFICANDO RUT DE ACUERDO A DÍGITO VERIFICADOR
#El usuario ingresa su RUT sin puntos ni guión, y el programa indica si es válido o no.
#Ejemplo: 12345678k
#El programa debe considerar que el RUT puede tener 8 o 9 dígitos (sin contar el dígito verificador).
#El dígito verificador puede ser un número del 0 al 9 o la letra 'k'.
#El programa debe validar el RUT utilizando el algoritmo oficial de cálculo del dígito verificador.


def verificar_rut():
    rut_invertido=""
    if len(rut)==9:
        for i in rut:
            rut_invertido=i+rut_invertido
        print(rut_invertido)
    elif len(rut)==8:
        rutCompleto="0"+rut
        for i in rutCompleto:
            rut_invertido=i+rut_invertido
        print(rut_invertido)
    else:
        print("Ingrese un rut correcto")
    a=int(rut_invertido[1])*2
    b=int(rut_invertido[2])*3
    c=int(rut_invertido[3])*4
    d=int(rut_invertido[4])*5
    e=int(rut_invertido[5])*6
    f=int(rut_invertido[6])*7
    g=int(rut_invertido[7])*2
    h=int(rut_invertido[8])*3
    sumaRut=(a+b+c+d+e+f+g+h)/11
    sumaRut2=int(sumaRut)
    sumaRutfinal=(a+b+c+d+e+f+g+h)-(sumaRut2*11)
    dig_verificador=11-sumaRutfinal
    dig_verificador=str(dig_verificador)
    if dig_verificador=="11":
        dig_verificador="0"
    elif dig_verificador=="10":
        dig_verificador="k"

    if len(rut)==9:
        if rut[8]==dig_verificador:
            print("Rut Válido")
        else: 
            print("Rut inválido")
    elif len(rut)==8:
        if rutCompleto[9]==dig_verificador:
            print("Rut Válido")
        else: 
            print("Rut inválido")
    else:
        print("Rut inválido")

rut=input("Ingrese nº rut sin guión ni puntos: ").lower()
verificar_rut()
