compañia = "Coding For All"
print(compañia)

print(len(compañia))

print(compañia.upper())

print(compañia.lower())

print(compañia.capitalize()) 
print(compañia.title()) 
print(compañia.swapcase()) 

print(compañia.split()[1:])

print(compañia.find('Coding')) 

print(compañia.replace('Coding', 'Python'))

compañia = compañia.replace('Coding', 'Python')
print(compañia)

print(compañia.split())

print(compañia[0])

print(len(compañia) - 1)

print(compañia[10])

acronimo1 = ''.join([word[0] for word in 'Python For Everyone'.split()])
print(acronimo1) 

acronimo2 = ''.join([word[0] for word in 'Coding For All'.split()])
print(acronimo2) 

posicion_C = compañia.find('C')
if posicion_C != -1:
    print(f"La posición de 'C' es: {posicion_C}")
else:
    print("No se encontró la letra 'C' en la cadena.")

posicion_F = compañia.find('F')
if posicion_F != -1:
    print(f"La posición de 'F' es: {posicion_F}")
else:
    print("No se encontró la letra 'F' en la cadena.")

print(compañia.rfind('l'))

oracion = 'No se puede terminar una oración con porque es una conjunción'
print(oracion.find('porque'))

print(oracion.rindex('porque'))

inicio = oracion.find('porque')
fin = oracion.rfind('porque') + len('porque')
print(oracion[inicio:fin])

print(compañia.startswith('Coding'))

print(compañia.endswith('All'))

bibliotecas = ['juanito', 'matraz', 'botella', 'Piramide', 'Aguila']
print('#'.join(bibliotecas))

print("\nliam\t19\tmexico\taguascalientes")

radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

print(f"7+ 6 = {7 + 6}")
print(f"4 - 6 = {4 - 6}")
print(f"7 * 6 = {7 * 6}")
print(f"3 / 6 = {3 / 6:.2f}")
print(f"5 % 6 = {5 % 6}")
print(f"8 // 6 = {8 // 6}")
print(f"1 ** 6 = {1 ** 6}")