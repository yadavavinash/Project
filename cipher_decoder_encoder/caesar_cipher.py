from logo import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
	cipher_text = ""
	for letters in plain_text:
		position = alphabet.index(letters)
		new_position = position + shift_amount
		new_letter = alphabet[new_position]
		cipher_text += new_letter
	print(f"your encoded text is {cipher_text}")
	 


def decrypt(plain_text,shift_amount):
	cipher_text = ""
	for letters in plain_text:
		position = alphabet.index(letters)
		new_position = position - shift_amount
		new_letter = alphabet[new_position]
		cipher_text += new_letter
	print(f"your decoded text is {cipher_text}")



if direction == "encode":
	encrypt(plain_text= text, shift_amount= shift)
elif direction == "decode":
	decrypt(plain_text=text, shift_amount=shift)
else:
	print("You have entered wrong input. Type 'encode' to encrypt, type 'decode' to decrypt:\n ")

# # other way 

# def cipher_text(plain_text, shift_amount, cipher_direction):
# 	end_text = ""
# 	for letters in plain_text:
# 		position = alphabet.index(letters)
# 		if direction=="decode":
# 			shift_amount *= -1
# 		new_position = position + shift_amount
# 		new_letter = alphabet[new_position]
# 		end_text += new_letter
# 	print(f"your {direction}d text is {end_text}.")

# cipher_text(plain_text= text, shift_amount= shift, cipher_direction= direction)



