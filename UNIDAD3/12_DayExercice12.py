# Nivel 1

import random

# Generar un identificador único alfanumérico de 8 caracteres
def generate_unique_id():
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz', k=8))

# Generar múltiples identificadores basados en las especificaciones del usuario
def generate_ids_by_user():
    char_count = int(input("¿Cuántos caracteres por ID?: "))
    id_count = int(input("¿Cuántos IDs deseas generar?: "))
    return [''.join(random.choices('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', k=char_count)) for _ in range(id_count)]

# Crear un código de color hexadecimal aleatorio
def generate_hex_color():
    return f"#{''.join(random.choices('abcdef0123456789', k=6))}"

# Nivel 2

# Crear una lista con varios códigos de color hexadecimal
def create_hex_color_list(quantity):
    return [generate_hex_color() for _ in range(quantity)]

# Crear una lista con varios códigos RGB
def create_rgb_color_list(quantity):
    return [f"rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})" for _ in range(quantity)]

# Generar colores según el formato solicitado (hexadecimal o RGB)
def generate_color_scheme(format_type, count):
    if format_type == 'hexadecimal':
        return create_hex_color_list(count)
    elif format_type == 'rgb':
        return create_rgb_color_list(count)
    else:
        return "Formato de color no reconocido."

# Nivel 3

# Reorganizar de manera aleatoria los elementos en una lista
def randomize_list(elements):
    random.shuffle(elements)
    return elements

# Generar una lista con 5 números únicos aleatorios dentro del rango de 1 a 15
def create_unique_random_list():
    return random.sample(range(1, 16), 5)