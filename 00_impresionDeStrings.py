name = "Rodrigo"
last_name= "Flores"
age = 22

template="Hola "+ name + last_name +" , tu edad es "+ age
print('v1 ', template)

template="Hola mi nombre es {} y mi apellido es {}".format(name,last_name)
print('v2',template)

print("v3 Hola "+ name + last_name +" , tu edad es "+ age)

template = f"Hola {name} {last_name}, tu edad es {age}"
print('v4',template)