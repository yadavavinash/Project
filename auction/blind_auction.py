
from logo import logo
print(logo)
import os
clear = lambda: os.system('clear')

print("\t\t welcome to blind auction lets place the bid.\n".upper())
bid_dictionay = {}
bidding_finished = False

def highest_bidder(bidding_record):
	#bidding recore ={"avinash: 123, "mohit":321}
	highest_bid = 0
	winner = ""
	for bidder in bidding_record:
		bid_amount = bidding_record[bidder]
		if bid_amount > highest_bid:
			highest_bid = bid_amount
			winner = bidder
	print(f"The winner is {winner} with  bid amout of ${highest_bid}.")

while not bidding_finished:
	name = input("Enter your name: ")
	amout = int(input("Enter the amount you want yo bid: $"))
	bid_dictionay[name] = amout
	should_continue =  input("Do you want to continue? Please enter 'Yes' or 'No'.\n").lower()
	if should_continue == "no":
		bidding_finished = True
		highest_bidder(bid_dictionay)
	elif should_continue == "yes":
		clear()
	

