import pyfiglet as pf

def print_border(length):
	for i in range(length):
		print("-----", end=" ")
	print()

def print_word(word):
	print_border(len(word))
	for letter in word:
		print(f"| {letter} |", end =" ")
	print() 
	print_border(len(word))

def print_board(board):
	for word in board:
		print_word(word)
		print()

if __name__ == "__main__":
	title = pf.figlet_format("WORDLE")
	print(title)
	word = "sneak"
	word_length = len(word)
	attempts = 0
	guesses = [" "*word_length for i in range(word_length)]
	print_board(guesses)
	while attempts < word_length:
		guess = input("Guess the word: > ")
		if len(guess) != word_length:
			print("Please, your guess word should be of length 5")
		elif not guess.isalpha():
			print("Please, your should only contains alphabetic characters")
		elif guess.isupper():
			print("Please, only lowercase characters are accepted")
		else:
			guesses[attempts] = guess
			print_board(guesses)
			attempts += 1
