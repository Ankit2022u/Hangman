import random
import words
import arts

# Selecting the word randomly
word_list = words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Create variables
end_of_game = False
lives = 6

# Printing Logo
print(arts.logo)

#Testing code
# print(f'Sssh, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f'\n"{guess}" is already guessed. Try something else.')

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # Testing Code
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print("\nWrong Guess")
        lives -= 1
        # User Lose
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The secret word was: {chosen_word}")
        else:
            print("\nRight Guess")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters i.e. User Won
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(arts.stages[lives])