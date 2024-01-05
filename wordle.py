import random
from termcolor import colored

def word_bank():
    wrd_bank = []
    data = open("words.txt")
    for line in data:
        for word in line.split():
            wrd_bank.append(word)
    data.close()
    return wrd_bank


def get_word():
    selection = word_bank()
    secret_word = random.choice(selection)
    print(secret_word)
    return secret_word


def duplicate_letters(input):
    letter_count = []
    for letter in input:
        if input.count(letter) > 1:
            if letter in letter_count:
                continue
            else:
                letter_count.append(letter)
    return letter_count

                
def turn_loop():
    answer = get_word()
    guess_choices = word_bank()
    guesses = 0               
    word_disp = []
    while guesses < 6:
        guess = input().lower()
        if len(guess) == 5 and guess in guess_choices:
            letter_count = duplicate_letters(guess)
            letter_disp = []
            if guess == answer:
                letter_disp.append(colored(guess, "green"))
                word_disp.append(''.join(letter_disp))
                print('\n'.join(word_disp))
                print(f"You guessed the word in {guesses + 1} guesses!")
                break
            else:
                green_letters = []
                for i in range(5):
                    if guess[i] in answer:
                        if guess[i] == answer[i]:
                            letter_disp.append(colored(guess[i], "green"))
                            if guess[i] in letter_count:
                                green_letters.append(guess[i])
                                letter_count.remove(guess[i])
                        else:
                            letter_count = duplicate_letters(guess)
                            if guess[i] not in letter_count:
                                if guess[i] not in green_letters:
                                    letter_disp.append(colored(guess[i], "yellow"))     
                                else:
                                    letter_disp.append(colored(guess[i], "white"))
                            elif guess[i] in letter_count:
                                if guess[i] not in green_letters:
                                    letter_disp.append(colored(guess[i], "yellow"))
                                    letter_count.remove(f'{guess[i]}')    
                                else:
                                    letter_disp.append(colored(guess[i], "white"))
                                    letter_count.remove(f'{guess[i]}')
                    else:
                        letter_disp.append(colored(guess[i], "white"))
                
                    
                guesses += 1
                word_disp.append(''.join(letter_disp))
                print('\n'.join(word_disp))            
        else:
            if len(guess) != 5:
                print("Guess must be 5 letters")
            elif guess not in guess_choices:
                print("Word is not in word list")
    if guesses == 6:
        print(f"The answer was {answer}")

    play_again = input("Press p to play again!").lower()
    if play_again == "p":
        turn_loop()
    
        
def game_loop():
    playing = True
    print(f"Welcome to wordle! \n Commands: \n -p to play \n -r for rules \n -q to quit")
    while playing == True:
        user_input = input().lower()
        if user_input == "p":
            turn_loop()
        elif user_input == "r":
            print("The rules are: \n You have 6 guesses to find the secret 5 letter word. \n If the letter is green the letter is in the correct place. \n If the letter is yellow, the letter is in the word but in the wrong spot. \n If the letter does not change, it is not in the word.")
            print("Press p to play or q to quit: ")
            continue
        elif user_input == "q":
            print("See you next time!")
            playing = False


if __name__ == '__main__':
    game_loop()