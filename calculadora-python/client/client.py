from server.operation import Operation

class Client:
    def validateOperation(operar, number1, number2):
        resultado = 0
        if operar == '1':
            resultado = Operation.Sumar(number1,number2)
        elif operar == '2':
            return Operation.Resta(number1,number2)
        elif operar == '3':
            return Operation.Multiplicacion(number1,number2)
        elif operar == '4':
            return Operation.Dividir(number1,number2)
        elif operar == '5':
            return Operation.Modulo(number1,number2)        
        elif operar == '6':
            return Operation.Exponente(number1,number2)
        return resultado

    def validateOtherOperation(operar, number1):
        resultado = 0                
        if operar == '7':
            return Operation.RaizCuadrada(number1)  
        elif operar == '8':
            return Operation.Factorial(number1)    
        return resultado
    