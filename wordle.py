import random

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

def split_word(x):
    return list(x)
    
#print(split_word("words"))

answer = get_word()
# ans_lst = split_word(answer)
guesses = 0
while guesses < 6:
    guess = input("Guess a word: ").lower()
    # guess_lst = split_word(guess)
    if len(guess) == 5 and guess in wrd_bank:
            if guess == answer:
                print("correct")
                print(f"You guessed the word in {guesses + 1} guesses!")
                break
            else:
                for i in range(5):
                    #check if letters in guess are in same spot as word
                    if guess[i] == answer[i]:
                        print(f"{guess[i]} is correct")
                    #check if letters in guess are in word
                    elif guess[i] in answer:
                        print(f"{guess[i]} is in word")

                #print("incorrect")
                guesses += 1
    else:
        if len(guess) != 5:
            print("Guess must be 5 letters")
        elif guess not in wrd_bank:
            print("Guess must be real word")
