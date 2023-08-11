from sympy import symbols, sympify #Librería para usar expresiones matemáticas

#Redondeo de cifras decimales definidas para los cálculos
redondeo = 6

#---- Listas usadas por Euler Mejorado y Rugen Kutta ----
lista_xn = [] #Lista para todos los valores de xn
lista_yn = [] #Lista para todos los valores de yn
lista_y = []  #Lista para todos los valores reales de la función y (solución de la ed)
#Errores
lista_ea = [] #Lista para todos los valores error absoluto
lista_er = [] #Lista para todos los valores error relativo
lista_ep = [] #Lista para todos los valores error porcentual

#---- Listas usadas solamente por Euler Mejorado ----
lista_m = []         #Lista para todos los valores de f(xn, yn)
lista_yAsterisk = [] #Lista para todos los valores de y*n+1
lista_mAsterisk = [] #Lista para todos los valores de f(xn+1, y*n+1)

#---- Listas usadas solamente por Runge Kutta ----
#Listas de Kn
lista_k1 = []
lista_k2 = []
lista_k3 = []
lista_k4 = []

#Función para evaluar expresiones matemáticas
def evaluar_expresion(expresion, variables):#Dada una expresion y variables definidas
    x, y = symbols('x y')#Definimos las variables x, y que son las que usaremos
    expr = sympify(expresion)#Convertimos la expresión a una expresión sympify
    resultado = expr.subs(variables)#Sustituimos los valores proporcionados de la expresión y hacemos el cálculo
    return resultado #La función devuelve el resultado de la expresión

#Función para el calculo de los errores
def calcularErrores():
    "Calculamos los errores"
    for yn, y in zip(lista_yn, lista_y):#Por cada yn, y en sus respectivas listas
        lista_ea.append(round(abs(y - yn), redondeo))#Error Absoluto    
        lista_er.append(round(lista_ea[-1] / abs(y), redondeo))#Error Relativo
        lista_ep.append(round(lista_er[-1]*100, redondeo))#Error Porcentual

#Función para "resetear" valores previos por cada problema
def limpiarListas(metodo):#Vaciamos las listas usadas dependiendo del método
    #---- Listas usadas por Euler Mejorado y Rugen Kutta ----
    lista_xn.clear() #Lista para todos los valores de xn
    lista_yn.clear() #Lista para todos los valores de yn
    lista_y.clear()  #Lista para todos los valores reales de la función y (solución de la ed)
    #Errores
    lista_ea.clear() #Lista para todos los valores error absoluto
    lista_er.clear() #Lista para todos los valores error relativo
    lista_ep.clear() #Lista para todos los valores error porcentual

    if metodo == "eulerMejorado":            
        #---- Listas usadas solamente por Euler Mejorado ----
        lista_m.clear()         #Lista para todos los valores de f(xn, yn)
        lista_yAsterisk.clear() #Lista para todos los valores de y*n+1
        lista_mAsterisk.clear() #Lista para todos los valores de f(xn+1, y*n+1)

    if metodo == "rungeKutta":    
        #---- Listas usadas solamente por Runge Kutta ----
        #Listas de Kn
        lista_k1.clear()
        lista_k2.clear()
        lista_k3.clear()
        lista_k4.clear()

#Función para mostrar los resultados de acuerdo al método
def mostrarResultados(metodo):
    # -- Común a ambos métodos --    
    print("Valores de xn")#Lista de xn
    for xn in lista_xn:
        print(xn)

    # -- Euler Mejorado --
    if metodo == "1":
        print("Valores de f(xn, yn)")
        for m in lista_m:#Lista de m
            print(m)
        print("Valores de f(xn+1, y*n+1)")
        for m_atc in lista_mAsterisk:#Lista de m asterisco
            print(m_atc)
        print("Valores de y*n+1")
        for y_atc in lista_yAsterisk:#Lista de y*n+1
            print(y_atc)
    
    # -- Runge Kutta --
    if metodo == "2":
        print("Valores de k1")#Lista de k1
        for k1 in lista_k1:
            print(k1)
        print("Valores de k2")#Lista de k2
        for k2 in lista_k2:
            print(k2)
        print("Valores de k3")#Lista de k3
        for k3 in lista_k3:
            print(k3)
        print("Valores de k4")#Lista de k4
        for k4 in lista_k4:
            print(k4)
    
    # -- Común a ambos métodos --
    print("Valores de yn")#Lista de yn
    for yn in lista_yn:
        print(yn)   
    print("Valores de y(x)")#Lista de y
    for y in lista_y:
        print(y)
    print("Valores de EA")#Lista de ea
    for ea in lista_ea:
        print(ea)
    print("Valores de ER")#Lista de er
    for er in lista_er:
        print(er)
    print("Valores de EP")#Lista de ep
    for ep in lista_ep:
        print(ep)