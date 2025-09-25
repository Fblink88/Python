
import csv
import json

#Clasificar las empresas
segmetacion_empresa={
    "Pequeño contribuyente" : [],
    "Mediano contribuyente" : [],
    "Gran contribuyente" : [],
}

#Leer datos desde el csv

with open("listadoRutEmpresa.csv", "r") as archivo:
    escritor = csv.DictReader(archivo)

    for fila in escritor:
        ventas = int(fila["Ventas"])
        clasificacion=None
        if ventas <= 100000000:
            clasificacion = "Pequeño contribuyente"
        elif ventas >100000000 and ventas <=200000000:
            clasificacion = "Mediano contribuyente"
        else:
            clasificacion = "Gran contribuyente"

        empresa = {
            "Rut" : fila["Rut"],
            "Nombre": fila["Nombre"],
            "Ventas": ventas
        }
        segmetacion_empresa[clasificacion].append(empresa)

#guardar los datos o listas en json

with open("segmentacionEmpresa.json", "w") as archivo:
    json.dump(segmetacion_empresa, archivo, indent=3)

print ("Json creado")