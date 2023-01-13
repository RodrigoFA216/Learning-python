import random
while True:
    options=('rock', 'scissors', 'paper')
    user_option=input('rock, scissors or paper?=> ')
    computer_option=random.choice(options)
    user_option.lower()
    if user_option in options:
        print(f"User option => {user_option}\nComputer Option => {computer_option}")
        if user_option==computer_option:
            print("tie")
        else:
            if user_option=='rock' and computer_option=='paper':
                print("Computer win")
            elif user_option=='rock' and computer_option=='cissors': 
                print("User win")
            elif user_option=='scissors' and computer_option=='paper': 
                print("User win")
            elif user_option=='scissors' and computer_option=='rock': 
                print("Computer win")
            elif user_option=='paper' and computer_option=='rock': 
                print("User win")
            elif user_option=='paper' and computer_option=='scissors': 
                print("Computer win")
    else:
        print("r u kidding bro?")