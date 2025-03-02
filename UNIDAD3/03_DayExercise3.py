edad = 19 
altura = 1.74  
num_comp = 5 + 7j  
print("Edad:", edad)
print("Altura:", altura)
print("Número complejo:", num_comp)

base = float(input("Introduce la base del triángulo: "))
altura_triangulo = float(input("Introduce la altura del triángulo: "))
area = 0.5 * base * altura_triangulo
print("El área del triángulo es:", area)

import math  
largo = float(input("Introduce el largo del rectángulo: "))
ancho = float(input("Introduce el ancho del rectángulo: "))

area_rectangulo = largo * ancho
perimetro_rectangulo = 2 * (largo + ancho)

print("Área del rectángulo:", area_rectangulo)
print("Perímetro del rectángulo:", perimetro_rectangulo)

radio = float(input("Introduce el radio del círculo: "))

pi = 3.14
area_circulo = pi * radio * radio
circunferencia = 2 * pi * radio

print("Área del círculo:", area_circulo)
print("Circunferencia del círculo:", circunferencia)


pendiente = 3
interseccion_x = 2 / 2  
interseccion_y = -2  

print("Pendiente de y = 7x - 5:", pendiente)
print("Intersección con eje X:", interseccion_x)
print("Intersección con eje Y:", interseccion_y)

x1, y1 = 7, 5
x2, y2 = 7, 4

pendiente_2 = (y2 - y1) / (x2 - x1)
distancia_euclidiana = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Pendiente entre (7,5) y (7,4):", pendiente_2)
print("Distancia euclidiana:", distancia_euclidiana)

print("¿Las pendientes son iguales?", pendiente == pendiente_2)

for x in range(-10, 10):
    y = x**2 + 6*x + 9
    if y == 0:
        print(f"y es 0 cuando x es {x}")

longitud_araña = len("araña")
longitud_lagartija = len("lagartija")

print("¿'araña' es más largo que 'lagartija'?", longitud_araña > longitud_lagartija) 

print("'on' está en 'python' y 'araña'?", "on" in "python" and "on" in "lagartija")

oracion = "Espero que este curso no sea aburrido."
print("'aburrido' está en la oración?", "aburrido" in oracion)

print("¿'encendido' no está en 'lagartija' ni en 'araña'?", "encendido" not in "lagartija" and "encendido" not in "araña")

longitud_python = len("python")
longitud_float = float(longitud_python)
longitud_string = str(longitud_float)

print("Longitud de 'python' como float:", longitud_float)
print("Longitud de 'python' como string:", longitud_string)

numero = int(input("Introduce un número para verificar si es par: "))
print("¿El número es par?", numero % 2 == 0)

print("¿7 // 3 es igual a int(2.7)?", 7 // 3 == int(2.7))

print("¿El tipo de '10' es igual al tipo de 10?", type("10") == type(10))

try:
    print("¿int('9.8') es igual a 10?", int("9.8") == 10)  
except ValueError:
    print("No se puede convertir '9.8' a entero.")

horas = float(input("Introduce las horas trabajadas: "))
tarifa = float(input("Introduce la tarifa por hora: "))

pago = horas * tarifa

print("El pago total es:", pago)

anios = int(input("Introduce el número de años: "))
segundos_por_año = 365 * 24 * 60 * 60
segundos_vividos = anios * segundos_por_año

print("Has vivido aproximadamente", segundos_vividos, "segundos.")

anios_maximos = 100
segundos_maximos = anios_maximos * segundos_por_anio

print("Si una persona vive 100 años, vivirá aproximadamente", segundos_maximos, "segundos.")

print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")

print("\nTabla generada dinámicamente:")
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)
