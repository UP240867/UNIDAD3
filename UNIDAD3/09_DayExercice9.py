# Nivel 1: Condicionales básicos y comparaciones

# 1. Verificar si el usuario tiene la edad suficiente para conducir
edad = int(input("Introduce tu edad para saber si puedes conducir: "))
if edad >= 18:
    print("¡Genial! Tienes la edad adecuada para conducir.")
else:
    print(f"Aún necesitas esperar {18 - edad} años para poder conducir.")

print("\n" + "-" * 40 + "\n")

# 2. Comparar la edad del usuario con la mía
mi_edad = 30  # Puedes ajustar esta edad
edad_usuario = int(input("¿Cuál es tu edad? "))
diferencia = abs(mi_edad - edad_usuario)
if edad_usuario > mi_edad:
    print(f"Eres {diferencia} años mayor que yo.")
elif edad_usuario < mi_edad:
    print(f"Soy {diferencia} años mayor que tú.")
else:
    print("¡Qué coincidencia! Tenemos la misma edad.")

print("\n" + "-" * 40 + "\n")

# 3. Comparar dos números introducidos por el usuario
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
if num1 > num2:
    print(f"{num1} es mayor que {num2}.")
elif num1 < num2:
    print(f"{num1} es menor que {num2}.")
else:
    print(f"{num1} y {num2} son iguales.")

print("\n" + "=" * 50 + "\n")

# Nivel 2: Calificaciones, estaciones y manejo de listas

# 1. Calificar estudiantes según su puntaje
puntaje = int(input("Introduce la puntuación del estudiante (0-100): "))
if 90 <= puntaje <= 100:
    print("Calificación: A")
elif 80 <= puntaje < 90:
    print("Calificación: B")
elif 70 <= puntaje < 80:
    print("Calificación: C")
elif 60 <= puntaje < 70:
    print("Calificación: D")
else:
    print("Calificación: F")

print("\n" + "-" * 40 + "\n")

# 2. Determinar la estación del año según el mes ingresado
mes = input("Introduce el nombre de un mes: ").lower()
if mes in ["marzo", "abril", "mayo"]:
    print("Estación: Primavera.")
elif mes in ["junio", "julio", "agosto"]:
    print("Estación: Verano.")
elif mes in ["septiembre", "octubre", "noviembre"]:
    print("Estación: Otoño.")
elif mes in ["diciembre", "enero", "febrero"]:
    print("Estación: Invierno.")
else:
    print("Mes no válido.")

print("\n" + "-" * 40 + "\n")

# 3. Manejo de una lista de frutas
frutas = ['manzana', 'naranja', 'mango', 'limón']
nueva_fruta = input("Introduce el nombre de una fruta: ").lower()
if nueva_fruta in frutas:
    print("Esa fruta ya existe en la lista.")
else:
    frutas.append(nueva_fruta)
    print("Fruta agregada. La lista actualizada es:", frutas)

print("\n" + "=" * 50 + "\n")

# Nivel 3: Trabajando con diccionarios complejos

# Diccionario que representa a una persona
persona = {
    'first_name': 'Carlos',
    'last_name': 'Ruiz',
    'age': 35,
    'country': 'Argentina',
    'is_married': False,
    'skills': ['Python', 'Django', 'JavaScript', 'React', 'SQL'],
    'address': {
        'street': 'Av. Siempre Viva',
        'zipcode': '1001'
    }
}

print("Información de la persona:")
for key, value in persona.items():
    print(f"{key}: {value}")

print("\n" + "-" * 40 + "\n")

# 1. Si existe la clave 'skills', mostrar la habilidad central
if 'skills' in persona and persona['skills']:
    indice_central = len(persona['skills']) // 2
    print("Habilidad central:", persona['skills'][indice_central])
else:
    print("No hay habilidades registradas.")

print("\n" + "-" * 40 + "\n")

# 2. Verificar si la persona tiene la habilidad 'Python'
if 'skills' in persona and 'Python' in persona['skills']:
    print("La persona tiene la habilidad Python.")
else:
    print("La persona no posee la habilidad Python.")

print("\n" + "-" * 40 + "\n")

# 3. Determinar el tipo de desarrollador según las habilidades
skills_set = set(persona['skills'])
if {'JavaScript', 'React'}.issubset(skills_set) and {'Python', 'Django'}.issubset(skills_set):
    print("Es un desarrollador Fullstack.")
elif {'JavaScript', 'React'}.issubset(skills_set):
    print("Es un desarrollador Frontend.")
elif {'Python', 'Django'}.issubset(skills_set):
    print("Es un desarrollador Backend.")
else:
    print("Título desconocido en el área de desarrollo.")

print("\n" + "-" * 40 + "\n")

# 4. Verificar el estado civil y la ubicación de la persona
if persona['country'].lower() == 'argentina':
    if persona['is_married']:
        print(f"{persona['first_name']} {persona['last_name']} está casado y vive en Argentina.")
    else:
        print(f"{persona['first_name']} {persona['last_name']} vive en Argentina y no está casado.")
else:
    print(f"{persona['first_name']} {persona['last_name']} no reside en Argentina.")
