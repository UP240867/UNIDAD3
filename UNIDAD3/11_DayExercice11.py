# Nivel 1

# Declarar una función que multiplique dos números
def multiply_two_numbers(x, y):
    return x * y

# Calcular el área de un rectángulo
def area_of_rectangle(length, width):
    return length * width

# Sumar todos los números en una lista
def sum_numbers_in_list(numbers):
    if all(isinstance(n, (int, float)) for n in numbers):
        return sum(numbers)
    return "Todos los elementos deben ser numéricos."

# Convertir grados Fahrenheit a Celsius
def convert_fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# Determinar la categoría según la edad
def categorize_age(age):
    categories = {
        'Niñez': range(0, 12),
        'Adolescencia': range(12, 18),
        'Adultez': range(18, 65),
        'Tercera Edad': range(65, 120)
    }
    for category, ages in categories.items():
        if age in ages:
            return category
    return "Edad no válida"

# Calcular la pendiente entre dos puntos
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

# Resolver una ecuación lineal
def solve_linear_eqn(a, b):
    if a == 0:
        return "No tiene solución o tiene infinitas soluciones."
    return -b / a

# Imprimir los elementos de una lista en líneas separadas
def print_elements(lst):
    for element in lst:
        print(element)

# Ordenar una lista al revés
def sort_list_reverse(lst):
    return sorted(lst, reverse=True)

# Convertir elementos de una lista a minúsculas
def lowercase_list_items(lst):
    return [item.lower() for item in lst]

# Agregar varios elementos a una lista
def add_items(lst, items):
    lst.extend(items)
    return lst

# Eliminar varios elementos de una lista
def remove_items(lst, items):
    return [item for item in lst if item not in items]

# Calcular el producto de todos los números en un rango
def product_of_numbers(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Calcular la suma de los números divisibles por 3 en un rango
def sum_of_multiples_of_three(n):
    return sum(i for i in range(n + 1) if i % 3 == 0)

# Calcular la suma de los números divisibles por 5 en un rango
def sum_of_multiples_of_five(n):
    return sum(i for i in range(n + 1) if i % 5 == 0)

# Nivel 2

# Contar números divisibles por 3 y por 5 en un rango
def count_multiples_of_three_and_five(n):
    multiples_of_three = sum(1 for i in range(n + 1) if i % 3 == 0)
    multiples_of_five = sum(1 for i in range(n + 1) if i % 5 == 0)
    return f"Números divisibles por 3: {multiples_of_three}. Números divisibles por 5: {multiples_of_five}."

# Calcular la potencia de un número
def power(base, exponent):
    return base ** exponent

# Verificar si una cadena está vacía
def is_string_empty(string):
    return len(string.strip()) == 0

# Calcular estadísticas básicas de una lista de datos
def calculate_minimum(lst):
    return min(lst)

def calculate_maximum(lst):
    return max(lst)

def calculate_sum(lst):
    return sum(lst)

def calculate_product(lst):
    result = 1
    for value in lst:
        result *= value
    return result

# Nivel 3

# Verificar si un número es perfecto
def is_perfect_number(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

# Verificar si una lista tiene elementos duplicados
def has_duplicates(lst):
    return len(lst) != len(set(lst))

# Verificar si todos los elementos de una lista son cadenas
def all_strings(lst):
    return all(isinstance(item, str) for item in lst)

# Verificar si una variable cumple con las reglas de identificación en Python
def is_valid_python_identifier(name):
    import keyword
    return name.isidentifier() and not keyword.iskeyword(name)

# Buscar los idiomas más estudiados (datos ficticios)
def most_studied_languages(n=5):
    language_stats = {'Inglés': 2000, 'Español': 700, 'Alemán': 400, 'Japonés': 350, 'Francés': 500}
    return sorted(language_stats.items(), key=lambda x: x[1], reverse=True)[:n]

# Buscar los países con mayor crecimiento demográfico (datos ficticios)
def fastest_growing_countries(n=5):
    growth_rate = {'India': 1.2, 'China': 0.5, 'Nigeria': 2.8, 'Pakistán': 2.0, 'Etiopía': 2.5}
    return sorted(growth_rate.items(), key=lambda x: x[1], reverse=True)[:n]