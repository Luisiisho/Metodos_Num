#Euler Mejorado
from subrutinas import lista_xn, lista_yn, lista_y, redondeo
from subrutinas import lista_m, lista_yAsterisk, lista_mAsterisk
from subrutinas import lista_ea, lista_er, lista_ep
from subrutinas import evaluar_expresion, calcularErrores, limpiarListas 

#Aquí desarrollamos el método
def eulerMejorado(datos):
    #Borramos valores previos
    limpiarListas("eulerMejorado")

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
    