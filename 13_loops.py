# while 
# has a structure like an if, 
# even if the condition was true the block of code will execute himself untill the condition was false. 
# Example, a program to count from 0 to 10
print("Count from 0 to 10")
i=0
while i<=10:
    print(f"Actual number was {i}")
    i+=1

# Example, a program to make the times table
x=int(input("Hi, what time table do you want to print => "))
i=0
while i<=10:
    print(f"{x} time {i} equals {x*i}")
    i+=1

# We can use breake for break the cycles
print("break the cycle")
i=0
while i<=10:
    print(f"Actual number was {i}")
    i+=1
    if i==5: # if the counter was 5
        break # break the cycle

# We can jump a cycle use continue
print("jump a cycle")
i=0
while i<=10:
    i+=1
    if (i%2)==(1):
        print(f"Actual number was {i}")
    else:
        continue # everything below this was ignored even the code was out of conditional

# count from 15 to 20
print("count from 15 to 20")
i=0
while i<=10:
    i+=1
    if i<15:
        continue
    print(f"Actual number was {i}")