#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Diccionario para representar un perro

perro = {
    "nombre": "Rocky", 
    "color": "Gris", 
    "raza": "Husky Siberiano", 
    "num_patas": 4, 
    "edad": 2
}

print("Datos del Perro:")
# Imprime cada clave y su valor asociado en el diccionario 'perro'
for clave, valor in perro.items():
    print(f"{clave}: {valor}")

print("\n" + "=" * 40 + "\n")

# Diccionario para representar un estudiante

estudiante = {
    "nombre": "María",
    "apellido": "González",
    "genero": "Femenino",
    "edad": 20,
    "estado_civil": "Soltera",
    "habilidades": ["Python", "Matemáticas", "Comunicación"],
    "pais": "España",
    "ciudad": "Madrid",
    "direccion": "Calle de la Luna, 10"
}

print("Datos Iniciales del Estudiante:")
for clave, valor in estudiante.items():
    print(f"{clave}: {valor}")

# Operaciones con el diccionario 'estudiante'

# 1. Obtener y mostrar la longitud del diccionario
longitud_estudiante = len(estudiante)
print("\nLongitud del diccionario estudiante:", longitud_estudiante)

# 2. Acceder a la lista de habilidades y verificar su tipo de dato
habilidades = estudiante["habilidades"]
print("\nHabilidades antes de la modificación:", habilidades)
print("Tipo de dato de 'habilidades':", type(habilidades))

# 3. Agregar nuevas habilidades a la lista de 'habilidades'
nuevas_habilidades = ["Inglés", "Trabajo en equipo"]
estudiante["habilidades"].extend(nuevas_habilidades)
print("\nHabilidades actualizadas:")
for habilidad in estudiante["habilidades"]:
    print("-", habilidad)

# 4. Obtener las claves y los valores del diccionario como listas
lista_claves = list(estudiante.keys())
lista_valores = list(estudiante.values())

print("\nLista de claves del diccionario 'estudiante':")
print(lista_claves)

print("\nLista de valores del diccionario 'estudiante':")
print(lista_valores)

# 5. Convertir el diccionario en una lista de tuplas usando el método items()
tuplas_estudiante = list(estudiante.items())
print("\nDiccionario 'estudiante' convertido a lista de tuplas:")
print(tuplas_estudiante)

# 6. Eliminar uno de los elementos del diccionario (eliminar 'estado_civil')
if "estado_civil" in estudiante:
    del estudiante["estado_civil"]
    print("\nDiccionario 'estudiante' después de eliminar 'estado_civil':")
    print(estudiante)
else:
    print("\nLa clave 'estado_civil' no existe en el diccionario.")

# Gestión final de variables

# Eliminar el diccionario 'perro'
del perro

# NOTA: Intentar imprimir el diccionario 'perro' después de borrarlo generaría un error.
# print(perro)  # Descomenta esta línea para verificar (generará un error)
