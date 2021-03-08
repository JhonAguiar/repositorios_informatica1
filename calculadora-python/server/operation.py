import math

class Operation(object):
    def Sumar(number1, number2):
        return number1+number2

    def Resta(number1,number2):
        return number1-number2

    def Multiplicacion(number1,number2):
        return number1*number2

    def Dividir(number1, number2):
        return number1/number2

    def Modulo(number1, number2):
        return number1%number2

    def Exponente(number1, number2):
        return number1**number2

    def RaizCuadrada(number1):
        return math.sqrt(number1)

    def Factorial(number1):
        return math.factorial(number1)