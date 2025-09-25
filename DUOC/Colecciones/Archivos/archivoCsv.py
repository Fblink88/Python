
import csv

with open("archivo_csv.csv", "w", newline="") as archivo_csv:
    escrito_csv=csv.writer(archivo_csv)
    escrito_csv.writerow(["Nombre", "Edad", "Comuna"])
    escrito_csv.writerows([
        ["Juan", 24, "Valpo"],
        ["Fabián", 35, "Villa Alemana"],
        ["Pedro", 30, "Quilpue"],
        ["Diego", 18, "Limache"],
        ["Fran", 29, "Quillota"]
    ])

#lectura de csv

with open("archivo_csv.csv", "r", newline="") as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for fila in lector_csv:
        for columna in fila:
            print (columna)