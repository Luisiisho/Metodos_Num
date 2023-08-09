from sympy import symbols, sympify

def evaluar_expresion(expresion, variables):
    x, y = symbols('x y')#Definimos las variables x, y
    expr = sympify(expresion)#Convertimos la expresión a una expresión sympify
    resultado = expr.subs(variables)#Sustituimos los valores proporcionados de la expresión
    return resultado

if __name__ == "__main__":
    expresion = input("Función: ")
    x_valor = float(input("x: "))
    y_valor = float(input("y: "))
                    
    variables = {'x': x_valor, 'y': y_valor}
    resultado = evaluar_expresion(expresion, variables)
    print("Resultado: ", resultado)