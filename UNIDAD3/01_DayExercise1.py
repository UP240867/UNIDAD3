print(9 + 7)
print(37 - 24)   
print(5 * 5)   
print(10 / 2)   
print(4 ** 2)  
print(56 % 4)  
print(8 // 2)

print(type(20))                  
print(type(10.14))                
print(type(7 + 8j))              
print(type('Juanito Pistolas'))          
print(type([7, 5, 4]))           
print(type({'Pedro Navajas':'Checoslovaquia'})) 
print(type({10.8, 5.12, 2.7}))    
print(type((7.5, 4.2, 7.2)))    
print(type(4 == 3))              
print(type(48 >= 3))    
print(type("juanito"))
print(type("alimaña"))
print(type("Durango"))
print(type(['luis', 'Python', 'Peru']))

entero = 10          
flotante = 9.8       
complejo = 4 - 4j    

cadena = "Hola, Python"

verdadero = True
falso = False

lista = [1, 2, 3, 4, 5]

tupla = (10, 20, 30, 40)

conjunto = {1, 2, 3, 4, 5}

diccionario = {"nombre": "Asabeneh", "país": "Finlandia", "edad": 30}

print(type(entero))
print(type(flotante))
print(type(complejo))
print(type(cadena))
print(type(verdadero))
print(type(falso))
print(type(lista))
print(type(tupla))
print(type(conjunto))
print(type(diccionario))

#calculo de distancia euclidiana 

import math

p1 = (2, 3)
p2 = (10, 8)

distancia = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

print("La distancia euclidiana entre", p1, "y", p2, "es:", distancia)