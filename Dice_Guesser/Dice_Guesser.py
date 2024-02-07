import random as random_throw


def roll_dice(dice_sides=6):
    return random_throw.randint(1, dice_sides)

def dice_guess(dice_guesses=0):
    print(f"======Welcome to the Guessing Dice======")
    print("----------------------------------------")

    player_name = input("Enter your name: ").capitalize()
    print(f"let's begin. {player_name}")
    pass

    while True:
        try:
            user_guess = int(input("Make a guess (1-6): "))
            if user_guess < 1 or user_guess > 6:
                print("Invalid input. Please enter a number between 1 and 6.")
                continue
                
            dice_roll = roll_dice()
            
            if user_guess != dice_roll:
                print(f"You got it wrong. The dice rolled {dice_roll}")
            else:
                print("You got it right!")
                dice_guesses += 1

        except ValueError:
            print("No names input.")
            continue

        play_again = input("Do you want to continue (y/n):").lower()
        if play_again != "y":
            break

    print(f"Thanks for playing the game {player_name}")


if __name__ == "__main__":
    dice_guess()
