import random
from termcolor import colored

wrd_bank = []
data = open("words.txt")
for line in data:
    for word in line.split():
        wrd_bank.append(word)
data.close()
#print(wrd_bank)
def get_word():
    secret_word = random.choice(wrd_bank)
    print(secret_word)
    return secret_word


#answer = get_word()


guesses = 0

answer = "slice"

def duplicate_letters(input):
    for letter in input:
        if input.count(letter) > 1:
            if letter in letter_count:
                continue
            else:
                letter_count.append(letter)
# duplicate_letters()
# print(letter_count)
word_disp = []
while guesses < 6:
    guess = input("Guess a word: ").lower()
    if len(guess) == 5 and guess in wrd_bank:
            if guess == answer:
                print(colored(guess, "green"))
                print(f"You guessed the word in {guesses + 1} guesses!")
                break
            else:
                letter_disp = []
                green_letters = []
                letter_count = []
                duplicate_letters(guess)
                for i in range(5):
                    if guess[i] in answer:
                        if guess[i] == answer[i]:
                            letter_disp.append(colored(guess[i], "green"))
                            if guess[i] in letter_count:
                                green_letters.append(guess[i])
                                letter_count.remove(guess[i])
                        else:
                            if guess[i] not in letter_count:
                                if guess[i] not in green_letters:
                                    letter_disp.append(colored(guess[i], "yellow"))
                                else:
                                    letter_disp.append(colored(guess[i], "white"))
                            
                            elif guess[i] in letter_count:
                                if guess[i] not in green_letters:
                                    letter_disp.append(colored(guess[i], "yellow"))
                                    letter_count.remove(guess[i])
                                else:
                                    letter_disp.append(colored(guess[i], "white"))
                                    letter_count.remove(guess[i])
                    else:
                        letter_disp.append(colored(guess[i], "white"))
                guesses += 1
                word_disp.append(''.join(letter_disp))
                print('\n'.join(word_disp))
                
                print(f"You have {6 - guesses} guesses left.")
        
                
                
                
                
    else:
        if len(guess) != 5:
            print("Guess must be 5 letters")
        elif guess not in wrd_bank:
            print("Word is not in word list")
