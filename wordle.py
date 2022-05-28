import pyfiglet as pf
from colorama import Fore, Style
import helper_functions

if __name__ == "__main__":
    title = pf.figlet_format("WORDLE")
    print(title)
    print("welcome! this is a terminal version of the well known wordle")
    menu = "type \"play\" to play the game or \"exit\" to exit the game > "
    won = False
    words, word = [], ""
    while True:
        choice = input(menu)
        words, word = helper_functions.get_word()
        if choice == "play":
            won  = helper_functions.play_wordle(words, "smile")
            if won:
    	        message = pf.figlet_format("Well Done!")
    	        print(f"{Fore.GREEN}{message}{Style.RESET_ALL}")
            else:
                print(f"the word was : {word}")
                message  = pf.figlet_format("Good luck next time!")
                print(f"{Fore.RED}{message}{Style.RESET_ALL}")
        elif choice == "exit":
            break
        else:
            print("Please enter a valid choice")
    print("thanks for playing, come back again soon")
