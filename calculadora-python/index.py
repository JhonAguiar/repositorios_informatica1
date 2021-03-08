from client.client import Client
#Método de entrada del programa.
def main():
    #Opciones para la calculadora.
    print("Ingrese los valores a operar.")
    print("1 - Suma.")
    print("2 - Resta.")
    print("3 - Multiplicación.")
    print("4 - Dividir.")
    print("5 - Módulo")
    print("6 - Exponente")
    print("7 - Raíz Cuadrada")
    print("8 - Factorial")
    #Ingreso de opción a ejecutar en la calculadora.
    operationToExcute = input("Ingrese número de valor a ejecutar: ")
    #Ingreso de primer valor.
    number1 = int(input("Ingrese valor uno: "))
    #Validación si requiere segundo valor.
    if operationToExcute == '1' or operationToExcute == '2' or operationToExcute == '3' or operationToExcute == '4' or operationToExcute == '5' or operationToExcute == '6':
        number2 = int(input("Ingrese valor dos: "))
    #Imprimir en consola el resultado
    if operationToExcute == '1' or operationToExcute == '2' or operationToExcute == '3' or operationToExcute == '4' or operationToExcute == '5' or operationToExcute == '6':
        print(Client.validateOperation(operationToExcute, number1, number2))
    elif operationToExcute == '7' or operationToExcute == '8':
        print(Client.validateOtherOperation(operationToExcute, number1))
    else:
        print("Esa operación no existe.")        

if __name__== '__main__':
    main()