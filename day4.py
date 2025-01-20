import random
user_choice = input("What do you choose? 0 for rock, 1 for paper, or 2 for scissors")

computer_choice = random.randint(0, 3)
print(f"Computer chose {computer_choice}")

if user_choice == 0 and computer_choice == 2:
    print("You win")
elif computer_choice == 0 and computer_choice == 0:
    print("You loose")
elif computer_choice > user_choice:
    print("You lose")
elif computer_choice < user_choice:
    print("You win")
elif computer_choice == user_choice:
    print("It's a draw")
else:
    print("Invalid number! You Loose")

