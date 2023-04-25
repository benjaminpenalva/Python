import math;

print("Calcular el tercer lado del triangulo")


PI = 3.1416

print("ingrese lados del triangulo")
b = float(input("lado b: "))
c = float(input("lado c: "))
print("ingrese el angulo en grados sexagesimales")
alfa = float(input())


a = (b**2 + c**2 - 2*b*c * math.cos(alfa*PI/180))**0.50


print("el lado a vale: ",a)