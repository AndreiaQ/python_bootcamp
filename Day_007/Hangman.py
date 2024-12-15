import random
import hangman_words
import hangman_art




chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder = ""



for x in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

game_over = False

correct_letters = []
guessed_letters = []

lives = 6

print(hangman_art.hangman_logo)

while not game_over:

    guess = input("Guess a letter: ").lower()

    print(f"************************************** {lives} /6 LIVES LEFT ***************************************")


    if guess in guessed_letters:
        print("You've already guessed ", guess)

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += guess
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

        guessed_letters.append(guess)



    print(display)

    if guess not in chosen_word:
        print("You've guessed " + guess + ", that's not in the word !\nYou lose a life")

        lives -= 1
        if lives == 0:
            game_over = True
            print("*************************************** YOU LOSE ****************************************")

    if "_" not in display:
        game_over = True
        print("*************************************** YOU WIN ****************************************")

    print(hangman_art.stages[lives])






