#Tres ejemplos de default parameters

def suma(a, b=5):
    suma = a+b
    print(f"Tu suma es {suma}")

def hola(nombre="Daniel"):
    print(f"Hola mi estimado {nombre}")

def trabajo(paga, puesto = "Gerente"):
    print(f"Tu puesto es {puesto}, y tu paga es de {paga}")

suma(2, 5)
hola()
trabajo(10000)

#los default parameters son parametros que no se moveran o el usuario no los pondra.