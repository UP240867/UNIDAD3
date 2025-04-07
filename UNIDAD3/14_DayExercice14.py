from functools import reduce
import random
from collections import Counter

# EJEMPLOS DE LISTAS PARA USAR
countries_list = ["Noruega", "Islandia", "Alemania", "Francia", "Italia", "España"]
names_list = ["Carlos", "Elena", "Sofia", "Martín"]
numbers_list = [3, 6, 9, 12, 15, 18, 21]

# 1. ITERACIÓN PARA MOSTRAR ELEMENTOS
for country in countries_list:
    print(f"País: {country}")

for name in names_list:
    print(f"Nombre: {name}")

for number in numbers_list:
    print(f"Número: {number}")

# 2. USANDO MAP PARA TRANSFORMAR DATOS
uppercase_countries = list(map(str.upper, countries_list))
names_reversed = list(map(lambda n: n[::-1], names_list))
numbers_tripled = list(map(lambda n: n * 3, numbers_list))

print(uppercase_countries)
print(names_reversed)
print(numbers_tripled)

# 3. USANDO FILTER PARA SELECCIONAR DATOS
countries_with_n = list(filter(lambda c: "n" in c.lower(), countries_list))
countries_short = list(filter(lambda c: len(c) < 7, countries_list))
countries_starting_I = list(filter(lambda c: c.startswith("I"), countries_list))

print(countries_with_n)
print(countries_short)
print(countries_starting_I)

# 4. OPERACIONES ENCADENADAS
result = reduce(lambda a, b: a + b,
                filter(lambda x: x > 50,
                       map(lambda x: x * x, numbers_list)))

print(f"Resultado de operaciones encadenadas: {result}")

# 5. EXTRAER SOLO ELEMENTOS NUMÉRICOS
def get_numeric_elements(data):
    return list(filter(lambda e: isinstance(e, (int, float)), data))

mixed_list = ["Texto", 42, 3.14, "Python", True, 100]
print(get_numeric_elements(mixed_list))

# 6. SUMA TOTAL DE NÚMEROS CON REDUCE
total_sum = reduce(lambda x, y: x + y, numbers_list)
print(f"Suma total: {total_sum}")

# 7. CONCATENAR ELEMENTOS EN UNA CADENA
joined_countries = reduce(lambda a, b: f"{a}, {b}", countries_list[:-1]) + f" y {countries_list[-1]} forman parte de Europa."
print(joined_countries)

# 8. FUNCIÓN PARA AGRUPAR PAÍSES POR CARACTERÍSTICA
def filter_countries(countries, keyword):
    return list(filter(lambda c: keyword.lower() in c.lower(), countries))

print(filter_countries(countries_list, "ia"))

# 9. CONTAR ELEMENTOS SEGÚN LA LETRA INICIAL
def count_elements_by_initial(data):
    result = {}
    for item in data:
        initial = item[0]
        result[initial] = result.get(initial, 0) + 1
    return result

print(count_elements_by_initial(countries_list))

# 10. FUNCIONES PARA OBTENER SUBLISTAS
def get_first_elements(data, count):
    return data[:count]

def get_last_elements(data, count):
    return data[-count:]

all_countries = ["Chile", "Argentina", "Uruguay", "Paraguay", "Perú", "Bolivia",
                 "Brasil", "Ecuador", "Colombia", "Venezuela", "Panamá", "México",
                 "Cuba", "Honduras", "Guatemala", "El Salvador", "Nicaragua", "Belice",
                 "Costa Rica", "República Dominicana"]

print(get_first_elements(all_countries, 5))
print(get_last_elements(all_countries, 5))

# PROCESAR PAÍSES DESDE UNA FUENTE EXTERNA
from external_dataset import countries_data  # Importa datos de un archivo externo

# 🔹 Ordenar países por atributo
def sort_countries_by_key(key):
    return sorted(countries_data, key=lambda c: c.get(key, ''))

# 🔹 Obtener idiomas comunes
def get_common_languages():
    languages = []
    for country in countries_data:
        languages.extend(country['languages'])
    return Counter(languages).most_common(5)

# 🔹 Obtener países con poblaciones altas
def get_top_populated_countries(n=5):
    return sorted(countries_data, key=lambda c: c['population'], reverse=True)[:n]

# Ejecutar funciones
if __name__ == "__main__":
    print("Países por nombre:", [c['name'] for c in sort_countries_by_key('name')][:5])
    print("Idiomas comunes:", get_common_languages())
    print("Top poblaciones:", [(c['name'], c['population']) for c in get_top_populated_countries()])