# A dictionary has a key and a value assigned for each key, 
# to get the definition of the value we need to reference the key 
# a dictionary can assign different types of valors for each key
# Dictionary on Python is an Object in JS

myDictionary={}
print(type(myDictionary))

person={
    "name": "Rodrigo",
    "age": 25,
    "Country": "México",
    "phone": "5544722244",
    "weight": 130.7
}

# we can use len like a string, list and touple
print(len(myDictionary))

# Need to a value assigned for a key? shure:
print(f"Hi, my name is {person['name']} my age are {person['age']}")

# caution, if the key not exists python will throw an error
# for this we use get function
print(person.get('height')) # reult: none

# we can ask first like this:
if 'height' in person: #this sentence evaluate if the key height exists
    print("avion are on dictionary")
else:
    print("avion aren't on dictionary")
    
# All the dictionary can be mutable with this functions:
# clear()	    Removes all the elements from the dictionary
# copy()	    Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	        Returns the value of the specified key
# items()	    Returns a list containing a tuple for each key value pair
# keys()	    Returns a list containing the dictionary's keys
# pop()	        Removes the element with the specified key
# popitem()	    Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	    Updates the dictionary with the specified key-value pairs
# values()	    Returns a list of all the values in the dictionary

developer={
    "name":"Rodrigo",
    "lastName":"Flores",
    "age":"23",
    "langs":["python", "js", "C", "C#"],
    "weight":85,
    "favouriteBand": "blink182"
}

developer["name"]="Santiago"
developer["age"]+=20
developer["langs"].append("typescript")

# Ways to delete a element
# Delete a key value
del developer["weight"]
developer.pop("favouriteBand")
print(list(developer.keys()))
print(list(developer.values()))