# ejercicio 1

tupla_vacia = ()

hermanas = ("melissa", "Fatima", "Karla")
hermanos = ("Alexis", "julio", "Luis")

todos_los_hermanos = hermanos + hermanas
print(todos_los_hermanos)

print(len(todos_los_hermanos))

familia_completa = todos_los_hermanos + ("Padre", "Madre")
print(familia_completa)

# ejercicio 2

*solo_hermanos, padre, madre = familia_completa
print(solo_hermanos, padre, madre)

frutas = ("guayaba", "Naranja", "pera")
verduras = ("Nabo", "ajo", "Batata")
productos_animales = ("carne", "pescado", "miel")

alimentos = frutas + verduras + productos_animales
print(alimentos)

lista_alimentos = list(alimentos)
print(lista_alimentos)

indice_medio = len(alimentos) // 2
elemento_medio = alimentos[indice_medio] if len(alimentos) % 2 != 0 else alimentos[indice_medio - 1: indice_medio + 1]

print(elemento_medio)

print(lista_alimentos[3:-3])

del alimentos