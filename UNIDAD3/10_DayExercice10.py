# Nivel 1: Operaciones básicas con iteraciones

# Iterar de 0 a 10 usando for y while
print("Iteración con for:")
for i in range(0, 11):
    print(f"Contador (for): {i}")

print("Iteración con while:")
i = 0
while i <= 10:
    print(f"Contador (while): {i}")
    i += 1

print("\n" + "-" * 40 + "\n")

# Iterar de 10 a 0 usando for y while
print("Iteración inversa con for:")
for i in range(10, -1, -1):
    print(f"Contador inverso (for): {i}")

print("Iteración inversa con while:")
i = 10
while i >= 0:
    print(f"Contador inverso (while): {i}")
    i -= 1

print("\n" + "-" * 40 + "\n")

# Imprimir un triángulo de 7 niveles
print("Triángulo de niveles:")
for i in range(1, 8):
    print("*" * i)

print("\n" + "-" * 40 + "\n")

# Imprimir un patrón de 8x8
print("Patrón 8x8:")
for _ in range(8):
    print("* " * 8)

print("\n" + "-" * 40 + "\n")

# Imprimir una tabla de multiplicación del 1 al 10
print("Tabla de multiplicación:")
for i in range(1, 11):
    print(f"{i} x {i} = {i * i}")

print("\n" + "-" * 40 + "\n")

# Iterar sobre una lista de tecnologías
tecnologias = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
print("Lista de tecnologías:")
for tech in tecnologias:
    print(f"Tecnología: {tech}")

print("\n" + "-" * 40 + "\n")

# Imprimir números pares e impares del 0 al 100
print("Números pares:")
for i in range(0, 101, 2):
    print(i)

print("Números impares:")
for i in range(1, 101, 2):
    print(i)

print("\n" + "=" * 50 + "\n")

# Nivel 2: Sumas y cálculos

# Sumar todos los números del 0 al 100
suma_total = sum(range(101))
print(f"La suma de todos los números del 0 al 100 es: {suma_total}.")

# Sumar los números pares e impares del 0 al 100
suma_pares = sum(i for i in range(0, 101) if i % 2 == 0)
suma_impares = sum(i for i in range(0, 101) if i % 2 != 0)
print(f"La suma de los números pares es {suma_pares}.")
print(f"La suma de los números")