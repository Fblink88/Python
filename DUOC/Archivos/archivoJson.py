
import json

datos=[
    {
    "Nombre" : "Juan",
    "Edad" : "25",
    "Comuna" : "Valpo",
    "Estudios" : ["Liceo A-1", "Duoc-UC", "Diplomado Duoc UC", "MIT", "NASA"]
},
{
    "Nombre" : "Pepe",
    "Edad" : "32",
    "Comuna" : "Viña",
    "Estudios" : ["Liceo A-2"]
},
]


with open("archivo2.json", "w") as archivo:
    json.dump(datos,archivo)

#Lectura de json

with open("archivo2.json", "r") as archivo:
    datos_leidos = json.load(archivo)

print(datos_leidos)