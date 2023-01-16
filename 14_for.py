# for was a specific structure that have more ways to use than each other sentence
# its like loop untill a condition was false and go away
for element in range(20): # for each element in range from 0 to 19
    print(element) # print the actual element

# for element in range(1,21):
#     print(element)

# we can use to loop and print each element from a list
myList = ['A', 'B', 'C', 'D', 'E', 'F']
for element in myList:
    print(element)

Tupla = ("Alfa", "Beta", "Gamma")
for element in Tupla:
    print(element)

developer={
    "name":"Rodrigo",
    "lastName":"Flores",
    "age":23,
    "langs":["python", "js", "C", "C#"],
}
for key in developer:
    print(key,  " => ", developer[key], " type => ", type(developer[key]))

# Another function be:
for key, value in developer.items():
    print(key, " => ", value, " type => ", type(value))

# Server response something like this
people=[
    {
        "name": "nico",
        "age": 24
    },
    {
        "name": "robby",
        "age": 20
    },
    {
        "name": "Andy",
        "age": 27
    }
]
for person in people:
    for name, age in person.items():
        print(name, " => ", age)

# fill all the empty lists with positive and negative numbers from list given
myList = [1, -1, 2, -2, 3, -3, 4, -4]
positiveList = []
negativeList=[]
for number in myList:
    if number<0:
        negativeList.append(number)
    else:
        positiveList.append(number)
print(negativeList)
print(positiveList)