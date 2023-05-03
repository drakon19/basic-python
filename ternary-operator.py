#Tres ejemplos de Ternary Operator 

def ejemplo1(energy):
    game_over = True if energy <= 0 else False
    print(game_over)

def ejemplo2 (numVisits):
    discount_perc = 20 if numVisits > 7 else 5

    print(f"tu descuento es de {discount_perc}%")

def ejemplo3 (num):
    numero = "par" if num%2==0 else "impar"
    print(f"Tu numero es {numero}")

ejemplo1(10)
ejemplo2(8)
ejemplo3(5)