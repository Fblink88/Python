
datos = """
    Curso 
"""
#Crear un archivo
with open('datos.txt','w') as archivo:
    archivo.write(datos)

#lextura de archivo txt opción 1

with open('datos.txt','r') as archivo:
    contenido = archivo.read()

print (contenido)

#lextura de archivo txt opción 2

archivo = open('datos.txt', 'r')
contenido = archivo.read()
print (contenido)
archivo.close()