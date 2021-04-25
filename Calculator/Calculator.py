from logo import logo
import os
clear = lambda: os.system('clear')

#add
def add(a,b):
	return a+b

#subtract
def subtract(a,b):
	return a-b

#divide
def divide(a,b):
	return a/b

# multiply
def multiply(a,b):
	return a*b

operations = {
 "+" :add,
 "-" :subtract,
 "/" :divide,
 "*" :multiply
}

def calculator(): # for reccursion
	print("\n\twelocome to the calculator ".upper(),logo)

	a = float(input("Enter the first number: "))

		
	for symbol in operations:
		print(symbol)
	continue_calculating = True 

	while continue_calculating:
		operation_symbol = input("pick an operation for the  line above: ")
		b = float(input("Enter the second number: "))
		calculation_function = operations[operation_symbol]
		result = calculation_function(a,b)

		print(f"{a} {operation_symbol} {b} = {result}")
		should_continue = input(f"type 'yes' to continue with {result} or 'no' to exit or 'new' for new calculation: ")
		if  should_continue == "yes":
			a = result
		elif should_continue == "new":
			continue_calculating = False
			clear()
			calculator()
		else:
			continue_calculating = False
			print("\n\n thank you".upper())

calculator()
