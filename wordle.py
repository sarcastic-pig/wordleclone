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


answer = get_word()
word_disp = ["_", "_", "_", "_", "_"]
letter_disp = []
guesses = 0
letter_count = []
green_letters = []

def duplicate_letters():
    for letter in answer:
        if answer.count(letter) > 1:
            if {letter :answer.index(letter)} in letter_count:
                continue
            else:
                letter_count.append({letter : answer.index(letter)})
# duplicate_letters()
# print(letter_count)
while guesses < 6:
    guess = input("Guess a word: ").lower()
    if len(guess) == 5 and guess in wrd_bank:
            if guess == answer:
                print("correct")
                print(f"You guessed the word in {guesses + 1} guesses!")
                break
            else:
                
                for i in range(5):
                    
                    if guess[i] in answer:
                        if guess[i] == answer[i]:
                            letter_disp.append(colored(guess[i], "green", "on_dark_grey"))
                            green_letters.append(guess[i])
                        else:
                            if guess[i] in answer:
                                letter_disp.append(colored(guess[i], "yellow", "on_dark_grey"))
                    else:
                        letter_disp.append(colored(guess[i], "white", "on_dark_grey"))
                print(' '.join(letter_disp))
                print(green_letters)


                #want to print out _____ with correct guesses inserted
                # for i in range(5):
                #     #check if letters in guess are in same spot as word
                #     if guess[i] == answer[i]:
                #         if word_disp[i] == "_":
                #                 word_disp[i] = guess[i]
                        
                #         #print(f"{guess[i]} is correct")
                #     #check if letters in guess are in word
                    
                #     #list does not need to populate if letter is in word_disp UNLESS there is a repeat letter // could check if first one is in place and then if it isnt that one is yellow and other is gray
                    
                #     elif guess[i] in answer:
                #         if guess[i] != word_disp[i]:
                #             if guess[i] in letter_disp:
                #                 continue
                #             elif guess[i] not in letter_disp:
                #                 letter_disp.append(guess[i])
                #     elif guess[i] in word_disp:
                #         letter_disp.remove(guess[i])

                #         #print(f"{guess[i]} is in word")
                # print(' '.join(word_disp))
                # print(' '.join(letter_disp))
                guesses += 1
                print(f"You have {6 - guesses} guesses left.")
    else:
        if len(guess) != 5:
            print("Guess must be 5 letters")
        elif guess not in wrd_bank:
            print("Word is not in word list")
