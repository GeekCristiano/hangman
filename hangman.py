import random

from hangman_words import hangman_words
from hangman_words import letters 
from hangman_arts import logo
from hangman_arts import stages 

print(logo)

lives = 6
chosen_word = random.choice(hangman_words) 
display = []
end_of_game = False

for letter in chosen_word:
    display += "_"

while not end_of_game:

    guess_letter = input("Guess a letter: ").lower()

    while not guess_letter in letters:
        print("Your input is incorrect! Please, input one letter.")
        guess_letter = input("Guess a letter: ").lower()

    if guess_letter in display:
        print(f"The character {guess_letter} has already been guessed.")
    
    if guess_letter in chosen_word: 
        for index in range(len(chosen_word)):
            current_letter = chosen_word[index]
            if current_letter == guess_letter:
                display[index] = guess_letter
        
        print(f"{' '.join(display)}")
    else:
        lives -= 1
        print(f"You gussed {guess_letter}, that's not in the word. You lose a life.")
       
        print(f"{' '.join(display)}")
        print(stages[lives])

        if lives == 0:
            print("You lose!")
            print(f"Hidden word is {chosen_word}.")
            end_of_game = True 
    
    if not "_" in display:
        end_of_game = True
        print("You win!")