#Importaciones
from eulerMejorado import eulerMejorado
from Runge_Kutta import rungeKutta
from subrutinas import mostrarResultados
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
                mostrarResultados(opcion)
            else:#Runge-Kutta
                rungeKutta(datos)
                #Mostramos los resultados de cada lista generada
                mostrarResultados(opcion)
        