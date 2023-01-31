# list = [1, 2, 3, 4, 5]
#     Can be mutable
#     each element was separated by a comma
#     it can have any datatype
# Lists methods
# list.method(index,element) o
# list.method(element)
# High priority methods
    # append(): Añade un ítem al final de la lista.
    # clear(): Vacía todos los ítems de una lista.
    # extend(): permite extender una lista agregándole los elementos de otra lista
    # count(): Cuenta el número de veces que aparece un ítem.
    # index(): Devuelve el índice en el que aparece un ítem (error si no aparece).
    # insert(): Agrega un ítem a la lista en un índice específico.
    # pop(): Extrae un ítem de la lista y lo borra.
    # remove(): Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos.
    # reverse(): Le da la vuelta a la lista actual.
    # sort(): Ordena automáticamente los ítems de una lista por su valor de menor a mayor.
# Actualizar un valor
# Lista = [1, 2, 3, 4, 5]
# Lista[0] = -8
# Lista = [-8, 2, 3, 4, 5], resultado de la lista luego de actualizar el valor
# Agregar un elemento
# Lista.append(indice,elemento) o
# Lista.append(elemento) en este caso el nuevo elemento se agrega al final de la lista
# Eliminar un elemento
# Lista.remove(indice, elemento)

my_list = ['A', 'B', 'C', 'D', 'E', 'F']

my_list.append('G')
my_list[0] = 'Z'
my_list.remove('C')
my_list.reverse()
print(my_list)