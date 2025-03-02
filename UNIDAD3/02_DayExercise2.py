print('hello word')
print(len('hello word'))
print(type('hello word'))
print(str(10))
print(int('10'))
print(float(10))
name = input('enter your name: ')
print('your name is ', name)
print(max(70, 50, 54, 13))
print(min(56, 67, 79,23))
data = (56, 45, 78, 89)
suma = sum(data, 45)
print(suma)
first_name = 'liam'
last_name = 'martinez'
country = 'Mexico'
age = '19'
is_married = 'false'
skills = ['Python', 'HTLM', 'CSS', 'React']
personal_info={  
    'name':'liam',
    'lastname': 'martinez',
    'country': 'Mexico',
    'city' : 'Ags',
    'age': '19',
    'married':'false',
    'skills': ('Python', 'HTLM', 'CSS', 'React'),

}
print(personal_info)
print('First name', first_name)
print('first name length',len(first_name))
print('last name:', len(last_name))
print('last name length:', len(last_name))
print('country: ', country)
print('age: ', age)
print('married:', is_married)
print('skills:', skills)
print('person information:', personal_info)


nombre = "liam"
apellido = "martinez "
nombre_completo = nombre + " " + apellido
pais = "México"
ciudad = "aguascalientes"
edad = 19
año = 2025
is_married = False
is_true = True
is_light_on = True

var1, var2, var3, var4 = 10, 20, "Python", False


# Verificar los tipos de datos
print(type(nombre))
print(type(apellido))
print(type(nombre_completo))
print(type(pais))
print(type(ciudad))
print(type(edad))
print(type(año))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print("Longitud del nombre:", len(nombre))

print("Diferencia de longitud:", len(nombre) - len(apellido))

num_one = 8
num_two = 6

total = num_one + num_two
diff = num_one - num_two
producto = num_one * num_two
division = num_one / num_two
resto = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

print("Suma:", total)
print("Resta:", diff)
print("Multiplicación:", producto)
print("División:", division)
print("Módulo:", resto)
print("Exponenciación:", exp)
print("División de piso:", floor_division)

radio = 30
pi = 3.1416

area_of_circle = pi * radio**2
circum_of_circle = 2 * pi * radio

print("Área del círculo:", area_of_circle)
print("Circunferencia del círculo:", circum_of_circle)


radio_usuario = float(input("Ingresa el radio del círculo: "))
area_usuario = pi * radio_usuario**2
print("El área del círculo con radio", radio_usuario, "es:", area_usuario)


nombre_usuario = input("Ingresa tu nombre: ")
apellido_usuario = input("Ingresa tu apellido: ")
pais_usuario = input("Ingresa tu país: ")
edad_usuario = int(input("Ingresa tu edad: "))

print("Nombre:", nombre_usuario)
print("Apellido:", apellido_usuario)
print("País:", pais_usuario)
print("Edad:", edad_usuario)

help('keywords')