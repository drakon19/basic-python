#Tres ejemplos de for loop with range()

def ejemplo0():
    for i in [1, 2, 3, 4]:
        print(i, end=", ") 

def ejemplo1(rango):
    # Ejemplo con un argumento
    for i in range(rango):
        print(i, end=", ")

def ejemplo2(inicio, parar):
    # Ejemplo con dos argumentos
    for i in range(inicio, parar):
        print(i, end=", ")
    
def ejemplo3(inicio, parar, paso):
    # Ejemplo con tres argumentos
    for i in range(inicio, parar, paso):
        print(i, end=", ")

ejemplo0()
ejemplo1(5)
ejemplo2(1,5)
ejemplo3(-1,5,2)