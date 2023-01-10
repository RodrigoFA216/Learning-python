# and y
print('AND')
print('True and True =>', True and True) # True
print('True and False =>', True and False) # False
print('False and True =>', False and True) # False
print('False and False =>', False and False) # False

print(10 > 5 and 5 < 10) # True
print(10 > 5 and 5 > 10) # False


stock = input('Ingrese el numero de stock ')
stock = int(stock)

print(stock >= 100 and stock <= 1000)

# or o
print('OR')
print('True or True =>', True or True) # True
print('True or False =>', True or False) # True
print('False or True =>', False or True) # True
print('False or False =>', False or False) # False

role = input('Digaita el rol => ')
print(role == 'admin' or role == 'seller') 

#not no
print ('NOT')
print('not true', not True)
print('not false', not False)

print('NOT AND')
print('True and True =>', not (True and True)) # False
print('True and False =>', not (True and False)) # True
print('False and True =>', not (False and True)) # True
print('False and False =>', not (False and False)) # True

stock = input('Ingrese el numero de stock =>')
stock = int(stock)

print(not (stock >= 100 and stock <= 1000))