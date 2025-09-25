print("")
print("*************************")
print("     Trivia 'Zelda'")
print("*************************")
print("           *      ")
print("          ***     ")
print("         *****    ")
print("       *       *  ")
print("      ***     ***  ")
print("     *****   ***** ")
print(" ")
print("*************************")
print("")
print("INSTRUCCIONES")
print("- Se presentarán 4 preguntas")
print("- Cada respuesta correcta otorga 1 punto ")
print("- Cada respuesta cercana otorga 0.5 puntos")
print("")

puntMayor=1
puntMenor=0.5
error=0
puntObtenido=0

print("A. ¿Cuál es el héroe del juego Zelda?")
print("1. Zelda")
print("2. Mario")
print("3. Link")
print("4. Fox")
respuesta=input("Escriba la respuesta ").capitalize().strip()

if respuesta=="Link":
    print("Respuesta correcta: Link.")
    puntObtenido=puntObtenido+puntMayor
else:
    if respuesta=="Zelda":
        print("Respuesta cercana. La respuesta correcta era Link.")
        puntObtenido=puntObtenido+puntMenor
    else:
        if respuesta=="Fox" or respuesta=="Mario":
            print("Respuesta incorrecta. La respuesta correcta era Link.")
        else:
            print("Respuesta inválida")
print("")
print("Tu puntaje hasta el momento es: ", puntObtenido)
print("")
print("B. ¿En qué consola salió el primer Zelda?")
print("1. NES")
print("2. SEGA")
print("3. SNES")
print("4. FDS")
respuesta=input("Escriba la respuesta ").upper()

if respuesta=="FDS":
    print("Respuesta correcta: FDS (Famicom Disk System)")
    puntObtenido=puntObtenido+puntMayor
else:
    if respuesta=="NES":
        print("Respuesta cercana. La respuesta correcta era FDS (Famicom Disk System)")
        puntObtenido=puntObtenido+puntMenor
    else:
        if respuesta=="SNES" or respuesta=="SEGA":
            print("Respuesta incorrecta. La respuesta correcta era FDS (Famicom Disk System)")
        else:
            print("Respuesta inválida")
print("")
print("Tu puntaje hasta el momento es: ", puntObtenido)
print("")
print("C. ¿Cómo se llama el último juego de Zelda?")
print("1. Ocarina of time")
print("2. The Hyrule Fantasy")
print("3. Tears of the Kingdom")
print("4. Breath of the Wild")
respuesta=input("Escriba la respuesta ").capitalize()
if respuesta=="Tears of the kingdom":
    print("Respuesta correcta: Tears of the Kingdom")
    puntObtenido=puntObtenido+puntMayor
else:
    if respuesta=="Breath of the wild":
        print("Respuesta cercana. La respuesta correcta era Tears of the Kingdom")
        puntObtenido=puntObtenido+puntMenor
    else:
        if respuesta=="The hyrule fantasy" or respuesta=="Ocarina of time":
            print("Respuesta incorrecta. La respuesta correcta era Tears of the Kingdom")
        else:
            print("Respuesta inválida")
print("")
print("Tu puntaje hasta el momento es: ", puntObtenido)
print("")
print("D. ¿Quién/que es Navi?(No hay respuesta cercana)")
print("1. Un pueblo")
print("2. Una hada")
print("3. Un caballo")
print("4. Una princesa")
respuesta=input("Escriba la respuesta ").capitalize()

if respuesta=="Una hada":
    print("Respuesta correcta: Una hada en Ocarina of time ")
    puntObtenido=puntObtenido+puntMayor
else:
    if respuesta=="Un pueblo" or respuesta=="Un caballo" or respuesta=="Una princesa":
            print("Respuesta incorrecta. La respuesta correcta era Una hada en Ocarina of time")
    else:
            print("Respuesta inválida")
print("")
print("Tu puntaje total es: ", puntObtenido)

if puntObtenido==4:
    print("FELICITACIONES HAS OBTENIDO EL PUNTAJE MÁXIMO")
else:
    if puntObtenido>0.5 and puntObtenido<4:
        print("AÚN FALTA POR APRENDER")
    else:
        print("NO SABES NADA SOBRE ZELDA")