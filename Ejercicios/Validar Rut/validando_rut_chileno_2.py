# Autor: Fabián Basaes
# Descripción: Verificador de RUT chileno MEJORADO
# Fecha: 25-09-2025


#SOLUCIÓN VERIFICANDO RUT DE ACUERDO A DÍGITO VERIFICADOR con FOR
#El usuario ingresa su RUT sin puntos ni guión, y el programa indica si es válido o no.
#Ejemplo: 12345678k
#El dígito verificador puede ser un número del 0 al 9 o la letra 'k'.
#El programa valida el RUT utilizando el algoritmo oficial de cálculo del dígito verificador.

def validar_rut_chileno(rut_completo):

    try:
        # 1. Limpiamos y preparamos la entrada
        rut_completo = rut_completo.lower().strip()
        
        cuerpo_rut = rut_completo[:-1]
        digito_verificador = rut_completo[-1]

        # --- NUEVA VALIDACIÓN ---
        # Verificamos que el cuerpo SÓLO contenga dígitos Y que su largo sea 7 u 8.
        if not cuerpo_rut.isdigit() or len(cuerpo_rut) not in [7, 8]:
            print("RUT Inválido: El RUT debe tener 8 o 9 caracteres (Ej: 12345678k o 1234567k).")
            return 
        
        # 3. Calculamos el dígito verificador 
        suma = 0
        multiplicador = 2
        # Se recorre el cuerpo del rut de manera inversa
        for digito in reversed(cuerpo_rut):
            suma += int(digito) * multiplicador
            multiplicador += 1
            #La validación se hace multipplicando por 2,3,4,5,6,7 y luego vuelve a 2
            if multiplicador == 8:
                multiplicador = 2

        resto = suma % 11 #Cálculo del resto de la división
        digito_calculado = 11 - resto
        
        if digito_calculado == 11:
            digito_esperado = "0"
        elif digito_calculado == 10:
            digito_esperado = "k"
        else:
            digito_esperado = str(digito_calculado) # Convertimos a string para comparar 


        # 4. Comparamos e imprimimos el resultado FINAL
        if digito_verificador == digito_esperado:
            print("RUT Válido")
        else:
            print("RUT Inválido: Dígito verificador no se corresponde con el RUT ingresado.")

    except IndexError:
        # Este error se activa si el usuario no ingresa nada
        print("RUT Inválido (no se ingresó un valor)")


# --- Programa principal ---
rut_usuario = input("Ingrese RUT sin guión ni puntos (ej: 12345678k): ")
validar_rut_chileno(rut_usuario)