import random
from logo import logo
import os
clear = lambda: os.system('clear')
EASY_LEVEL_TURN = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess,number,turns):
	'''Chech answers agaunst guess returns the no of turen remaining'''
	if guess > number:
		print("Too High!")
		return turns -1
	elif guess < number:
		print("Too Low!")
		return turns -1
	else:
		print(f"You got it rght! The asnwer was {guess}")

def set_dificulty():
	dificulty_level = input("choose a dificulty. Type 'easy' or 'hard': ").lower()
	if dificulty_level == "easy":
		return EASY_LEVEL_TURN
		
	elif dificulty_level == "hard":
		return HARD_LEVEL_TURNS
		
		
def game():
	print(logo)
	print("welcow to the number guessing game! ")
	print("I'm thinking of a number between 1 and 100. ")
	numbers= range(1,100)
	number = random.choice(numbers)
	# print(number)

	turns = set_dificulty()
	
	guess = 0
	while guess!= number:
		print(f"you have {turns} attemps remaining to guess the number. ")
		guess = int(input("Guess the Number: "))
		
		turns = check_answer(guess,number,turns)
		if turns == 0:
			print("You've run out of gusses tou lose! ")
			return
		elif guess != number:
			print("Guess again! ")


while input("\nDo you wanna play Guess the number game? type 'Y' or 'N': ").lower()== "y":
	clear()
	game()

