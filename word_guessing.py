import random
def choose_word():
    words=["python","coding","portfolio","courses"\
        "programming","code","data","visual","studio"]
    return random.choice(words)

# print( choose_word())
def word_status(word,guessed_letters):
    display=""
    for letter in word:
        if letter in guessed_letters:
            display+= letter
        else:
            display+="_"
    return display

def word_guessing_game():
    secret_word=choose_word()
    guessed_letters=[]
    attempts=7
    
    print("Word Guessing Game")
    print("******************")
    print("Secretword:",word_status(secret_word, guessed_letters))
    
    while attempts>0:
        guess=input("Guess A Letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha(): 
            print("you must enter a single letter.")
            continue
        if guess in guessed_letters:
            print("you already guessed that letter")
        
        guessed_letters.append(guess)  
        
        if guess not in secret_word:
            attempts -=1
            print(f"you have '{guess}' occurs in the word.")    
            print(f"you have {attempts} attemps remaining.")
            
        else:
            occurences=secret_word.count(guess)
            print(f"Letter '{guess}' occurs {occurences} times.")
            
        current_status=word_status(secret_word, guessed_letters)
        print("Secret Word:",current_status)
        
        if "_" not in current_status:
            print("Congratulations! You guessed the word.")
            break
    if "_" in current_status:
        print(f"you ran out of the attempts")
word_guessing_game()