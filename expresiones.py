from sympy import symbols, sympify

def evaluar_expresion(expresion, variables):
    x, y = symbols('x y')#Definimos las variables x, y
    expr = sympify(expresion)#Convertimos la expresión a una expresión sympify
    resultado = expr.subs(variables)#Sustituimos los valores proporcionados de la expresión
    return resultado