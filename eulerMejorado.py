from expresiones import*

#Método Euler Mejorado
lista_xn = []#Lista para todos los valores de xn
lista_yn = []#Lista para todos los valores de yn
lista_m = []#Lista para todos los valores de f(xn, yn)
lista_yAsterisk = []#Lista para todos los valores de y*n+1
lista_mAsterisk = []##Lista para todos los valores de f(xn+1, y*n+1)
lista_y = []#Lista para todos los valores reales de la función y (solución de la ed)
lista_ea = []#Lista para todos los valores error absoluto
lista_er = []#Lista para todos los valores error relativo
lista_ep = []#Lista para todos los valores error porcentual

#Lista de las listas, para generar la tabla --- Pendiente
#tabla = [lista_xn, lista_yn, lista_m, lista_yAsterisk, lista_mAsterisk, lista_y, lista_ea, lista_er, lista_ep] ---- Pendiente

#Redondeo de cifras decimales
redondeo = 6#digítos decimales

def calcularErrores():
    "Calculamos los errores"
    for yn, y in zip(lista_yn, lista_y):
        lista_ea.append(round(abs(y - yn), redondeo))#Error Absoluto    
        lista_er.append(round(lista_ea[-1] / abs(y), redondeo))#Error Relativo
        lista_ep.append(round(lista_er[-1]*100, redondeo))#Error Porcentual

def procesarDatos(datos):
    #Añadimos los elementos que ya tenemos a sus respectivas listas
    lista_xn.append(round(datos["x0"],redondeo))#El primer xn, que sería x0
    lista_yn.append(round(datos["y0"],redondeo))#El primer yn, que sería y0
    lista_y.append(round(datos["y0"],redondeo))#También agregamos y0 a la lista de y reales
    
    #Calculamos la primera pendiente de una vez
    variables = {'x': lista_xn[0], 'y': lista_yn[0]}#Sustituimos los valores de x0, y0 a la expresión f(xn, yn)
    pendienteAnterior = evaluar_expresion(datos["y'"], variables)#Cálculo de f(xn, yn)
    lista_m.append(round(pendienteAnterior, redondeo))#Añadimos la pendiente a la lista de pendientes
    
    while lista_xn[-1] != datos["aprox"]:#Mientras el último dato de la lista todavía no llege a la aproximación deseada
        #Primero calculamos y*n+1 = yn + hf(xn,yn)                
        lista_yAsterisk.append(round(lista_yn[-1] + datos["h"]*pendienteAnterior, redondeo))#Metemos y*n+1 a su lista
        
        #Generamos el siguiente xn (sumando h) --> Lo que determina la siguiente iteración del ciclo
        lista_xn.append(round(lista_xn[-1] + datos["h"], redondeo))#Lo guardamos en su lista
        
        #Calculamos yn+1 = yn + h*((f(xn, yn) + f(xn+1, y*n+1))/2)
        variables = {'x': lista_xn[-1], 'y': lista_yAsterisk[-1]}#Sustituimos xn actual y y*n+1 actual
        pendienteActual = evaluar_expresion(datos["y'"], variables)#Cálculo de f(xn+1, y*n+1)
        lista_mAsterisk.append(round(pendienteActual, redondeo))#Guardamos f(xn+1, y*n+1) en su lista
        sumaPendientes = pendienteAnterior + pendienteActual#La suma de las pendientes
        lista_yn.append(round(lista_yn[-1] + datos["h"]*(sumaPendientes/2), redondeo))#Guardamos el valor de yn en su lista

        #Calculamos la siguiente pendiente
        variables = {'x': lista_xn[-1], 'y': lista_yn[-1]}#Sustituimos los valores últimos de xn, yn a la expresión f(xn, yn)
        pendienteAnterior = evaluar_expresion(datos["y'"], variables)#Cálculo de f(xn, yn)
        lista_m.append(round(pendienteAnterior, redondeo))#Añadimos la pendiente a la lista de pendientes
        
        #Ahora calculamos los valores reales de la función y(x) (solución de la ed)
        variables = {'x': lista_xn[-1], 'y': 0}#Sustituimos xn actual, yn es lo que se busca calcular
        lista_y.append(round(evaluar_expresion(datos["y(x)"], variables), redondeo))#Calculamos y(x) y guardamos en su lista
    
    #Calculamos los errores
    calcularErrores()