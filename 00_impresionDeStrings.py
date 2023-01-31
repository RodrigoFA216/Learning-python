name = "Rodrigo"
last_name= "Flores"
age = 22

#Creas un string y luego lo mandas a imprimir
template="Hola "+ name + last_name +" , tu edad es "+ age 
print('v1 ', template)

#creas un string y con la función format introduces los valores en las llaves {}
template="Hola mi nombre es {} y mi apellido es {}".format(name,last_name)
print('v2',template)

#imprimir todo concatenando strings y datos
print("v3 Hola "+ name + last_name +" , tu edad es "+ age)

#usar la función format como f al inicio del string como si fuera un parámetro de template
template = f"Hola {name} {last_name}, tu edad es {age}"
print('v4',template)

print(f"V5 Hola {name} {last_name}, tu edad es {age}")