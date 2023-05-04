#Tres ejemplos de keyword arguments

def team(name, project):
    print(name, "esta trabajando en", project)

def hola(nombre):
    print(f"Hola mi estimado {nombre}")

def trabajo(paga, puesto):
    print(f"Tu puesto es {puesto}, y tu paga es de {paga}")


team(project ='Edpresso', name = "Daniel")
hola(nombre = "Yoshio")
trabajo(paga = 10000,puesto = "gerente")

#Son los argumentos que cuando los mandamos a llamar en el def, usamos = para la asignacion directa
