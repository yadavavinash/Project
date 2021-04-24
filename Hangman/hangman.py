import random
import os
clear = lambda: os.system('clear')


from words_list_module import words
from hangman_logo import logo
print("\t\t welcome to hangman game \n\n".upper())
choosen_word = random.choice(words)
len_choosen_word = len(choosen_word)
lives = 0
# print(logo)

# test
# print(f"your word is {choosen_word}\n")
print(f"it's a {len_choosen_word} letter word.")

display = []
for i in choosen_word:
	display += '_'
print(display)

end_of_game = False



while not end_of_game:
	guess = input("guess a letter \n\n".lower())
	clear()
	if guess in choosen_word:
		print(f"you have guessed correct letter, now guess the next  letter {guess} \n\n")

	for position in range(len_choosen_word):
		letter = choosen_word[position]
		# print(f"current position{position}\n, current letter{letter}\n, guessd word {guess}")
		if letter == guess:
			display[position] = letter


	if guess not in choosen_word:
		print(f"{guess} is not the correct word, you lost a life\n")
		lives += 1
		if lives ==6:
			end_of_game = True
			print(f"you lose\n the correct word is {choosen_word}".upper())

	print(f"{''.join(display)}")

	if "_" not in display:
		end_of_game = True
		print("You win\n".upper()) 
	from hangman_logo import stages
	print("\n",stages[lives])
