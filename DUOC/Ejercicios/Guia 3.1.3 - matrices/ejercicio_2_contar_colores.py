# El cubo 3x3x3 
cubo = [
    [["rojo", "amarillo", "Verde"], 
     ["Blanco", "rojo", "Naranja"], 
     ["amarillo", "rojo", "Blanco"]],

    [["Naranja", "Verde", "rojo"], 
     ["rojo", "amarillo", "amarillo"], 
     ["Verde", "Blanco", "rojo"]],

    [["Blanco", "amarillo", "Verde"], 
     ["rojo", "Naranja", "Naranja"], 
     ["amarillo", "Verde", "rojo"]]
]

# Crear una variable para cada color para luego contar
contador_amarillo = 0
contador_rojo = 0
contador_naranja = 0
contador_verde = 0
contador_blanco = 0

# Contador 
for capa in cubo:
    for fila in capa:
        for color in fila:
            if color == "amarillo":
                contador_amarillo += 1
            elif color == "rojo":
                contador_rojo += 1
            elif color == "Naranja":
                contador_naranja += 1
            elif color == "Verde":
                contador_verde += 1
            elif color == "Blanco":
                contador_blanco += 1

# Paso 3: Mostrar los resultados manualmente
print("--- Conteo de Colores (con variables separadas) ---")
print(f"Número de elementos \"amarillo\": {contador_amarillo}")
print(f"Número de elementos \"rojo\": {contador_rojo}")
print(f"Número de elementos \"Naranja\": {contador_naranja}")
print(f"Número de elementos \"Verde\": {contador_verde}")
print(f"Número de elementos \"Blanco\": {contador_blanco}")