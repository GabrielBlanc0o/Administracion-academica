'''nombre = input("Ingrese el nombre del estudiante: ")

nota=[]
x=0
y=0

estudiante[x]=input("Ingrese el nombre del estudiante: ")
nota[y]=float(input("Ingrese la nota del estudiante: "))
promedio[x]=(nota[y]+nota[y+1]+nota[y+2])/3
'''

def registrar_estudiante(nombre, edad, n1, n2, n3):
    return nombre, edad, n1, n2, n3   

def calcular_promedio(n1, n2, n3):
    promedio = (n1 + n2 + n3) / 3
    return promedio
