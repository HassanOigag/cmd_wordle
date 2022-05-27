import pyfiglet as pf
from string import ascii_lowercase as alpha


def print_border(word_length):
    for i in range(word_length):
        print("-----", end=" ")
    print()


def print_word(word):
    print_border(len(word))
    for letter in word:
        print(f"| {letter} |", end=" ")
    print()
    print_border(len(word))


def print_board(words_board):
    for word in words_board:
        print_word(word)
        print()


def check_guess(word, guess):
    #
    status = []
    for index, letter in enumerate(guess):
        if letter in word:
            if guess[index] == word[index]:
                # 1 means the letter is in the word and its correct spot
                status.append(1)
            else:
                # 2 means the letter is in the word but in a wrong spot
                status.append(2)
        else:
            status.append(0)  # 0 means the letter is not in the actual word
    return status


if __name__ == "__main__":
    print(check_guess("hello", "hello"))
    # title = pf.figlet_format("WORDLE")
    # print(title)
    # word = "sneak"
    # word_length = len(word)
    # attempts = 0
    # guesses = [" "*word_length for i in range(word_length)]
    # wrong_letters = []
    # print_board(guesses)
    # while attempts < word_length:
    # 	guess = input("Guess the word: > ")
    # 	if len(guess) != word_length:
    # 		print("Please, your guess word should be of length 5")
    # 	elif not guess.isalpha():
    # 		print("Please, your should only contains alphabetic characters")
    # 	elif guess.isupper():
    # 		print("Please, only lowercase characters are accepted")
    # 	else:
    # 		guesses[attempts] = guess
    # 		print_board(guesses)
    # 		attempts += 1
