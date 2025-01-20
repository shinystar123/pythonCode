import random

word_list = ["aardvark", "baboon", "camel"]


lives = 6


chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(1, 6):
    placeholder += "_"
print(placeholder)

game_over = False



while not game_over:
    correct_letters = []

    guess = input("Guess a letter: ").lower()

    display = ""



    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)

        elif letter in correct_letters:
            display += guess

        else:
            display += "_"
    print(display)

    if "_" not in display:
        game_over = True
        print("You win")


    if guess not in chosen_word: 
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose.")



