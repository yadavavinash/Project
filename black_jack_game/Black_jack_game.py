import random
import os
clear = lambda: os.system('clear')
from logo import logo

def deal_card():
	'''Return a random card from the deck'''
	cards = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
	card = random.choice(cards)
	return card

def caclulate_score(cards):
	"""Returns a random card from the deck."""

	if sum(cards)==21 and len(cards) ==21:
		return 0

	if 11 in cards and sum(cards)> 21:
		cards.remove(11)
		cards.append(1)
	
	return sum(cards)

def compare(user_score,computer_score):
	
	if user_score == computer_score:
		return "Draw 🙃"
	elif computer_score == 0:
		return "Lose, opponent has Blackjack 😱 " 
	elif user_score == 0:
		return "Win with a Blackjack 😎"
	elif user_score > 21:
		return "You went over. You lose 😭"
	elif computer_score > 21:
		return "Opponent went over. You win 😁"
	elif user_score > computer_score:
		return "You win 😃"
	else:
		return "You lose 😤"	


def play_game():
	print(logo)

	user_card =[]
	computer_card = []
	is_game_over = False


	for i in range(2):
		user_card.append(deal_card())
		computer_card.append(deal_card())

	while not is_game_over:
		user_score = caclulate_score(user_card)
		computer_score = caclulate_score(computer_card)
		print(f"your card:{user_card}, current_score ={user_score}")
		print(f"computer card:{computer_card[0]}")

		if user_score == 0 or computer_score ==0 or user_score > 21:
			is_game_over= True
		else:
			user_should_deal = input("\nType 'y' to draw another card, type 'n' to pass: \n").lower()
			if user_should_deal =="y":
				user_card.append(deal_card())
			else:
				is_game_over = True
			
	while computer_score !=0 and computer_score < 17:
		computer_card.append(deal_card())
		computer_score = caclulate_score(computer_card)

	print(f"\nyor final hand: {user_card} and your final score in {user_score} ".upper())
	print(f"\ncomputer final hand is {computer_card} and computer final score is {computer_score}".upper())
	print(compare(user_score,computer_score))

while input("\nDo you wanna play game of blackjack? type 'Y' or 'N': ").lower()== "y":
	clear()
	play_game()