# Programa para evaluar si un numero es automata

dont_stop = True  #Vamos a repetir el ciclo hasta que se cumpla un proceso y decidamos pararlo

while dont_stop:
    num = int(input("Ingresa un numero: "))

    def decimal_a_binario(num):

        if num == 0:
            return ""

        else:
            return str(num % 2) + decimal_a_binario(num // 2)

    binario = decimal_a_binario(num)[::-1]
    print(binario)

    if binario[:4] == '1010':

        print("El valor binario es apto")

    else:
        print("El valor ingresado no es apto!")

    dont_stop = input("¿Desea continuar?: ") == "si"
