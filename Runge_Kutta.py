#Rugen-Kutta
from expresiones import*
from eulerMejorado import redondeo, calcularErrores

#Listas de Kn
lista_k1 = []
lista_k2 = []
lista_k3 = []
lista_k4 = []

lista_xn = [] #Lista para las xn
lista_yn = [] #Lista para las yn
lista_y = []  #Lista para los valores reales de y

#Listas de errores
lista_ea = [] #Error absoluto
lista_er = [] #Error relativo
lista_ep = [] #Error porcentual

def rungeKutta(datos):
    limpiarListas() #Eliminamos datos previos
    
    #Guardamos los datos ya obtenidos
    lista_xn.append(round(datos["x0"], redondeo)) #x0 a su lista xn
    lista_yn.append(round(datos["y0"], redondeo)) #y0 a su lista yn

    iteraciones = round(datos["aprox"] + datos["h"], redondeo)

    #Mientras xn todavía no llegue a la aproximación
    while lista_xn[-1] != iteraciones:
        #Calculamos k1
        variables = {'x': lista_xn[-1], 'y': lista_yn[-1]} #Sustituimos xn y yn
        k1 = evaluar_expresion(datos["y'"], variables) #Calculamos f(xn, yn)
        lista_k1.append(round(k1, redondeo)) #Guardamos k1 en su lista

        #Calculamos k2
        k2_xn = lista_xn[-1] + (1/2)*datos["h"]    #xn + (1/2)h
        k2_yn = lista_yn[-1] + (1/2)*datos["h"]*k1 #yn + (1/2)hk1
        variables = {'x': k2_xn, 'y': k2_yn} #Sustituimos k2_xn y k2_yn
        k2 = evaluar_expresion(datos["y'"], variables) #Calculamos f(k2_xn, k2_yn) --> f(xn + (1/2)h, yn + (1/2)hk1)
        lista_k2.append(round(k2, redondeo)) #Guardamos k2 en su lista

        #Calculamos k3
        k3_xn = lista_xn[-1] + (1/2)*datos["h"]    #xn + (1/2)h
        k3_yn = lista_yn[-1] + (1/2)*datos["h"]*k2 #yn + (1/2)hk2
        variables = {'x': k3_xn, 'y': k3_yn} #Sustituimos k3_xn y k3_yn
        k3 = evaluar_expresion(datos["y'"], variables) #Calculamos f(k3_xn, k3_yn) --> f(xn + (1/2)h, yn + (1/2)hk2)
        lista_k3.append(round(k3, redondeo)) #Guardamos k3 en su lista

        #Calculamos k4
        k4_xn = lista_xn[-1] + datos["h"] # xn + h
        k4_yn = lista_yn[-1] + datos["h"]*k3 #yn + hk3
        variables = {'x': k4_xn, 'y': k4_yn} #Sustituimos k4_xn y k4_yn
        k4 = evaluar_expresion(datos["y'"], variables) #Calculamos f(k4_xn, k4_yn) --> f(xn + h, yn +hk3)
        lista_k4.append(round(k4, redondeo)) #Guardamos k4 en su lista

        #Calculamos yn+1        
        #yn+1 = yn + (h/6)*(k1 + 2k2 + 2k3 + k4)        
        lista_yn.append(round(lista_yn[-1] + (datos["h"]/6)*(k1 + 2*k2 + 2*k3 + k4), redondeo))

        #Calculamos y real
        variables = {'x': lista_xn[-1], 'y': 0} #Sustituimos xn
        y = evaluar_expresion(datos["y(x)"], variables) #Calculamos y(x)
        lista_y.append(round(y, redondeo)) #Guardamos y en su lista de y reales

        #Calculamos la siguiente xn (siguiente iteración)
        lista_xn.append(round(lista_xn[-1] + datos["h"], redondeo)) #xn+1 = xn + h

    #Quitamos los datos que estan de más
    lista_yn.pop() #La última yn guardada
    lista_xn.pop() #El último xn guardado
    #Calculamos los errores
    calcularErrores()   


def limpiarListas():
    #Limpiamos listas de Ks
    lista_k1.clear()
    lista_k2.clear()
    lista_k3.clear()
    lista_k4.clear()
    
    #Limpiamos listas de errores
    lista_ea.clear()
    lista_er.clear()
    lista_ep.clear()

    #Lo demás
    lista_xn.clear()
    lista_yn.clear()
    lista_y.clear()