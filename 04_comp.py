# > 
print(7 > 3)
print(3 > 7)
print(7 > 7)

# <
print(5 < 6)
print(6 < 5)
print(5 < 5)

# >=
print(2 >= 1)
print(2 >= 3)
print(2 >= 2)

# <=
print(1 <= 2)
print(2 <= 1)
print(2 <= 2)

# ==

print(6 == 6)
print(5 == 2)

# !=

print(6 != 10)
print(6 != 6)

print("Apple" == 'Apple')
print("Apple" == 'apple')
print("1" == 1)

age = 15
print(age >= 18)

a=2
b=3

#and
print(a&b)#2 10 & 11 => 10

#or
print(a|b)#3 10 | 11 => 11

#xor
print(a^b)#1 10 ^ 11 => 01

#not
print(~a)#-3 ~(00000010) => (11111101)

#desplazamiento

#Realiza un desplazamiento a la derecha bit a bit. Desplaza los bits del operador de la izquierda a la derecha 
# tantos bits como indica el operador de la derecha
print(a>>b)#0 00000010 >> 00000011 = 0

#Realiza un desplazamiento a la izquierda bit a bit. Desplaza los bits del operando de la izquierda a la izquierda 
# tantos bits como especifique el operador de la derecha
print(a<<b)#16 00000010 << 00000011 = 00001000

#operadores de pertenencia

# Un operador de pertenencia se emplea para identificar pertenencia en alguna secuencia (listas, strings, tuplas).
# in y not in son operadores de pertenencia.
# in devuelve True si el valor especificado se encuentra en la secuencia. En caso contrario devuelve False.
# not in devuelve True si el valor especificado no se encuentra en la secuencia. En caso contrario devuelve False.

a = [1,2,3,4,5]
#Esta 3 en la lista a?
print(3 in a) # Muestra True 

#No está 12 en la lista a?
print(12 not in a) # Muestra True

str = "Hello World"

#Contiene World el string str?
print("World" in str) # Muestra True

#Contiene world el string str? (nota: distingue mayúsculas y minúsculas)
print("world" in str) # Muestra False  

print("code" not in str) # Muestra True

#Operadores de identidad
# Un operador de identidad se emplea para comprobar si dos variables emplean la misma ubicación en memoria.
# is y is not son operadores de identidad.
# is devuelve True si los operandos se refieren al mismo objeto. En caso contrario devuelve False.
# is not devuelve True si los operandos no se refieren al mismo objeto. En caso contrario devuelve False.
# Ten en cuenta que dos valores, cuando son iguales, no implica necesariamente que sean idénticos.

a = 3
b = 3  
c = 4
print (a is b) # muestra True
print (a is not b) # muestra False
print (a is not c) # muestra True

x = 1
y = x
z = y
print (z is 1) # muestra True
print (z is x) # muestra True

str1 = "FreeCodeCamp"
str2 = "FreeCodeCamp"

print (str1 is str2) # muestra True
print ("Code" is str2) # muestra False

a = [10,20,30]
b = [10,20,30]

print (a is b) # muestra False (ya que las listas son objetos 
# mutables en Python así que se guardan en otro lugar distinto) 