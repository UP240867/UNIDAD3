# Nivel 1

import random

# Generar un identificador de usuario único de 8 caracteres
def generate_user_identifier():
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890', k=8))

# Crear múltiples identificadores según las preferencias del usuario
def create_user_identifiers():
    char_length = int(input("¿Cuántos caracteres para el ID?: "))
    id_count = int(input("¿Cuántos IDs necesitas?: "))
    return [''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890', k=char_length)) for _ in range(id_count)]

# Crear un color en formato HSL aleatorio
def hsl_color_generator():
    return f"hsl({random.randint(0, 360)},{random.randint(0, 100)}%,{random.randint(0, 100)}%)"

# Nivel 2

# Crear una lista de colores en formato hexadecimal
def hex_color_palette(size):
    return [f"#{''.join(random.choices('abcdef0123456789', k=6))}" for _ in range(size)]

# Crear una lista de colores HSL
def hsl_color_palette(size):
    return [hsl_color_generator() for _ in range(size)]

# Generar colores con formato personalizado
def create_color_palette(format_type, amount):
    if format_type == 'hex':
        return hex_color_palette(amount)
    elif format_type == 'hsl':
        return hsl_color_palette(amount)
    else:
        return "Formato de color no soportado"

# Nivel 3

# Reordenar de forma aleatoria elementos de una lista
def randomize_elements(list_data):
    random.shuffle(list_data)
    return list_data

# Crear una lista de 6 números únicos entre 0 y 15
def unique_random_sample():
    return random.sample(range(16), 6)

# Filtrar números positivos de una lista
def filter_positive_numbers(data):
    return [value for value in data if value > 0]

# Descomponer una lista de listas
def decompose_nested_list(nested_data):
    return [element for sublist in nested_data for element in sublist]

# Crear una lista de potencias de números
def generate_power_tuples():
    return [(i, i**2, i**3, i**4) for i in range(1, 10)]

# Mapear países y ciudades con detalles estructurados
def map_countries_to_dict(countries):
    return [{'pais': pais.upper(), 'ciudad': ciudad.title()} for grupo in countries for pais, ciudad in grupo]

# Función lambda para calcular el área de un triángulo
calculate_triangle_area = lambda base, height: 0.5 * base * height