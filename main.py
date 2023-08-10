#Importaciones
from eulerMejorado import*
from Runge_Kutta import*

def mostrarMenu():
    print("(1) Euler Mejorado")
    print("(2) RUNGE-KUTTA")
    print("(3) Salir")
    opcion = input()
    return opcion

def pedirDatos():

    #Pedimos la función diferencial/derivada primera de y
    derivada_y = input("y': ")
    #Pedimos la función solución a la ecuación diferencial    
    funcion_y = input("y(x): ")
    #Pedimos los valores del PVI: y(x0) = y0
    x0 = input("PVI:\n\tx0: ")
    y0 = input("\ty0: ")
    #Pedimos el incremento deseado
    h = input("h: ")
    #Pedimos la aproximación requerida
    aprox = input("Aproximación: ")
    #Guardamos los datos en un diccionario para retornarlos y procesarlos después
    #De una vez los convertimos a tipo float
    datos = {"y'": derivada_y, "y(x)": funcion_y, "x0": float(x0), "y0":float(y0), "h": float(h), "aprox": float(aprox)}
    return datos

def mostrarResultadosM1():
    print("Valores de xn")#1
    for xn in lista_xn:
        print(xn)
    print("Valores de yn")#2
    for yn in lista_yn:
        print(yn)            
    print("Valores de f(xn, yn)")#3
    for m in lista_m:
        print(m)
    print("Valores de y*n+1")#4
    for y_atc in lista_yAsterisk:
        print(y_atc)
    print("Valores de f(xn+1, y*n+1)")#5
    for m_atc in lista_mAsterisk:
        print(m_atc)
    print("Valores de y(x)")
    for y in lista_y:
        print(y)
    print("Valores de EA")
    for ea in lista_ea:
        print(ea)
    print("Valores de ER")
    for er in lista_er:
        print(er)
    print("Valores de EP")
    for ep in lista_ep:
        print(ep)

def mostrarResultadosM2():
    print("Valores de xn")#Lista de xn
    for xn in lista_xn:
        print(xn)
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

if __name__ == "__main__":
    #El programa se mantiene activo mientras el usuario no quiera salir de él
    salir = False
    while salir == False:
        #Mostramos el menu con las opciones
        opcion = mostrarMenu()
        if opcion == '3':#Si se quiere salir
            salir = True#Salimos
        elif opcion == '1' or opcion == '2':#Para cualquiera de los dos métodos
            datos = pedirDatos()#Pedimos los mismos datos y los guardamos
            if opcion == '1':#Euler Mejorado
                #Procesamos los datos para el euler mejorado
                eulerMejorado(datos)
                #Mostramos los resultados de cada lista generada
                mostrarResultadosM1()
            else:#Runge-Kutta
                rungeKutta(datos)
                #Mostramos los resultados de cada lista generada
                mostrarResultadosM2()
        