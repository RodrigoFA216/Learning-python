while True:
    user_option=input('rock, scissors or paper?=> ')
    if user_option.isalpha():
        user_option=user_option.lower()
    computer_option='paper'
    if user_option==computer_option:
        print("tie")
    else:
        if user_option=='rock':
            print("I win")
        elif user_option=='scissors': 
            print("you win")
        else:
            print("what are you playing bro?")