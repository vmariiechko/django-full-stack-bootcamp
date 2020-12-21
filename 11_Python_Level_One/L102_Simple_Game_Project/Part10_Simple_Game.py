###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!

# Generate computer code
import random
def generate_code():
	digits = [str(num) for num in range(10)]
	random.shuffle(digits)
	return digits[:3]

# Get guess
def get_guess():
	return list(input("What is your guess? "))

# Generate the clues
def generate_clue(random, guess):
	if guess == random:
		return "WICTORY!"

	clues = []

	for i,num in enumerate(guess):
		if num == random[i]:
			clues.append("Match")
		elif num in code:
			clues.append("Close")

	if clues == []:
		return ["Nope"]
	else:
		return clues

# Game logic
print("Welcome!")

code = generate_code()

clue_report = []

while clue_report != "WICTORY!":

	guess = get_guess()

	clue_report = generate_clue(code, guess)

	for clue in clue_report:
		print(clue)

