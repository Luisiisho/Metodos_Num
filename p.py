l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
l3 = [9, 10]
l4 = [11, 12, 13, 14, 15]

listas = [l1, l2, l3, l4]

tabla = []
filaImprimir = ""#Fila a imprimir
numF = 0#Número de fila (iterador de filas)
filasE = 0#Filas existentes en la tabla

#Primero nos interesa saber cuantas filas tendrá la tabla
for lista in listas:
    for elemento in lista:
        filasE += 1
        tabla.append([])
    break
for lista in listas:
    for elemento in lista:
        if numF < filasE:            
            tabla[numF].append(elemento)
            numF += 1            
    numF = 0

print(tabla)


for fila in tabla:
   for elemento in fila:
      filaImprimir += f"{elemento}\t"
   print(filaImprimir)
   print()
   filaImprimir = ""