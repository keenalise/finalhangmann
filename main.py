from randomWords import random_words
from hangmanArts import display_hangman


# Main function to play the game
def play():
    word = random_words() # get a random word
    word_completion = '_' * len(word) 
    # String with underscores representing unguessed letters
    guessed = False
    guessed_letters = [] # to store the letter that user input
    guessed_words = [] # to store the word that is found
    tries = 6

    print(" Yoooooooo!")
    print("Let's play hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0: 
        # if true and number of tries is greater than 0
        guess = input("Please guess a letter or word: ").lower()
        #convert input to lower case letters
        if len(guess) == 1 and guess.isalpha(): # if the word is already guessed
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess) #add to the list of guessed letters
            else:
                print("Good job,", guess, "is in the word!") # if the word is correct 
                guessed_letters.append(guess)
                word_as_list = list(word_completion) 
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = ''.join(word_as_list)
                if '_' not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            #if whole world is guessed and it is alphabets
            if guess in guessed_words: # if the words is in list of already guessed
                print("You already guessed the word", guess)
            
            elif guess != word: # if the words is not in the word
                print(guess, "is not the word.")
                tries -= 1  # number of tries is decreased
                guessed_words.append(guess) 
            else:
                guessed = True
                word_completion = word 
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!") 
        # if the words are guessed successfully
    else:
        print(f"Sorry, you ran out of tries. The word was ## {word} ##.")
        print("Maybe next time!")
        # if maximum number of tries is reached
        
        
# Run the game
if __name__ == "__main__":
    play()