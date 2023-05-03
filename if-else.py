#Tres ejemplos sobre if else 

def ejemplo1 (numero1, numero2):
    a = numero1
    b = numero2

    if a > b:
        print("El primer numero es mayor que el segundo")
    else:
        print("El primer numero es menor o igual que el segundo")

def ejemplo2 (num):
    if num % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")

def ejemplo3 (puesto, salario_base):
    if puesto == "Gerente":
        salario = salario_base * 1.2
    elif puesto == "Supervisor":
        salario = salario_base * 1.1
    else:
        salario = salario_base

    print(f"El salario de {puesto}, es: {salario}")

ejemplo1(3, 5)
ejemplo2(4)
ejemplo3("Gerente", 35000)