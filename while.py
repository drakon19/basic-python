#Tres ejemplos de while

def ejemplo1(contador):
# Inicializamos el contador
    i = contador

# Bucle while para imprimir los números
    while i < 5:
        print(i)
        i += 1

def ejemplo2(num):
# Inicializamos el número
    numero = num

# Buscamos el primer número par
    while numero % 2 != 0:
        numero += 1

    print(f"El primer número par mayor que cero es: {numero}")

def ejemplo3(contador, suma):
# Inicializamos el contador y la suma
    i = contador
# Bucle while para sumar los números
    while i <= 10:
        suma += i
        i += 1

    print("La suma de los números del 1 al 10 es:", suma)

ejemplo1(3)
ejemplo2(0)
ejemplo3(1, 0)