import logo
game = [logo.rock,logo.paper,logo.scissor]

user_choice = int(input("please choose a number! rock  = 0, paper = 1, scissors = 2 \n"))
print(game[user_choice])


import random

computer_choice = random.randint(0,2)
print("\t computer choice:".upper())
print(game[computer_choice])



if user_choice>=3 or user_choice<0:
    print("wrong input, you lost")
elif user_choice==0 and computer_choice==2:
    print("you win!")
elif computer_choice==0 and user_choice==2:
    print("you lose")
elif computer_choice > user_choice:
    print("you lose")
elif user_choice > computer_choice:
    print("you won")
elif computer_choice == user_choice:
    print("it's a draw")
