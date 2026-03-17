'''
resolviendo dudas
nombre = input("Ingrese el nombre del estudiante: ")

nota=[]
x=0
y=0

estudiante[x]=input("Ingrese el nombre del estudiante: ")
nota[y]=float(input("Ingrese la nota del estudiante: "))
promedio[x]=(nota[y]+nota[y+1]+nota[y+2])/3
'''

estudiantes = []
nota1 = []
nota2 = []
nota3 = []
promedios = []

def calcular_promedio(n1, n2, n3):
    return (n1 + n2 + n3) / 3

def estado(prom):
    if prom >= 4.0:
        return "Aprobado"
    elif prom >= 3.0:
        return "En recuperación"
    else:
        return "Reprobado"

def registrar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    estudiantes.append(nombre)

    n1 = float(input("Ingrese nota 1: "))
    n2 = float(input("Ingrese nota 2: "))
    n3 = float(input("Ingrese nota 3: "))

    nota1.append(n1)
    nota2.append(n2)
    nota3.append(n3)

    prom = calcular_promedio(n1, n2, n3)
    promedios.append(prom)

# comentado porque no se usa en el menú actual

# def ver_promedio():
#     if len(estudiantes) == 0: # usando len para verificar que no sea equivalente a 0
#         print("Primero registre un estudiante")
#         return
#     # Se accede al último promedio registrado
#     print(f"Promedio de {estudiantes[-1]}: {round(promedios[-1], 2)}") para redondear valor flotante

# comentado porque no se usa en el menú actual

# def ver_estado(): 
#     if len(estudiantes) == 0:
#         print("Primero registre un estudiante")
#         return
#     est = estado(promedios[-1])
#     print(f"Estado de {estudiantes[-1]}: {est}")

def mostrar_todos():
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados")
        return

    print("\n=== ESTUDIANTES REGISTRADOS ===")
    for i in range(len(estudiantes)):
        print(f"\nNombre: {estudiantes[i]}")
        print(f"Nota 1: {nota1[i]}")
        print(f"Nota 2: {nota2[i]}")
        print(f"Nota 3: {nota3[i]}")
        print(f"Promedio: {round(promedios[i], 2)}")
        print(f"Estado: {estado(promedios[i])}")

while True:
    print("\n===== SISTEMA DE ESTUDIANTES =====")
    print("1. Registrar estudiante")
    print("2. Mostrar todos los estudiantes")
    print("3. Salir")

    opcion = int(input("Seleccione una opción: \n "))

    if opcion == 1:
        registrar_estudiante()


    elif opcion == 2:
        mostrar_todos()


    elif opcion == 3:
        print("Saliendo del sistema...")
        break
        
    else:
        print("Opción inválida")
