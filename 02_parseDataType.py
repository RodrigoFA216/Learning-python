#int to string
age=23
print("I'm " + str(age) + " years old")
    #This is how {} works
print(f"i'm {age} years old")

#string to int
    #an input catch all like strings
age=input("how old are you? => ")
age=int(age)
print(f"on 10 years you will be {age+10} years old")
    #!!! Caution, you can't parse a letter to number