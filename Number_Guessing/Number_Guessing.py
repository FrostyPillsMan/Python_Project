import random as random_num_guess


user_attempts: int = 0
rand_num_end: int = 10
user_guess_lst: list[int] = []
user_attempt_lst: list[int] = []
"""Represents a storage value.
"""


def show_score(user_guess_lst : list[int]) -> None:
    print(f"The current score is {len(user_guess_lst)} attempts") 
    # Display total number of attempts.


def start_game(user_responds : str, user_play : str) -> None:
    rand_num = random_num_guess.randint(1, rand_num_end)
    # Random number generates from {1-10}.
    
    while user_responds.lower() == "yes":
        try:
            user_guess = int(input("Enter the number between 1 - 10: "))
            if user_guess < 1 or user_guess > 10:
                # Guesses checking condition.
                raise ValueError(
                    "Please guess the number within a range."
                )
                # Display an error message. 
            
            global user_attempts
            # Modify value inside function.
            user_attempts += 1
            user_attempt_lst.append(user_attempts)
            # Track down user attempts.
            

            if user_guess == rand_num:
                user_guess += 1
                user_guess_lst.append(user_guess)
                print("Voila! You found it...")
                print(f"It took you {user_attempts} trial run")
                play_again = input("Would you like to play one more time {}"
                      .format("(Yes/No)")).lower()
                if play_again.lower() != "yes":
                    print("That\'s fine :), have a nice day {}".format(user_play))
                    exit()
                    # Exit the game immediately.
                else:
                    user_attempts = 0
                    # Reset attempts from the scoreboard.
                    show_score(user_guess_lst)
                    # Display Current scoreboard.
                    continue
            
            if user_guess > rand_num:
                print("It\'s lower")
            elif user_guess < rand_num:
                print("It\'s higher")

        except ValueError as err:
            print("Oops! Invalid value accepted, try again...")
            print(err)
        # Invalid input, Outside the checking range condition.


def game() -> None:
    print("-----------------------------")
    print("welcome to the guessing game.".title())
    print("-----------------------------")

    user_play = input("Enter your name please : ").capitalize()
    user_responds = input(
        f"Hi!!, {user_play}, Would you like to play the awesome guessing game?\n" 
        f"Pick one (Yes/No) -->").lower()

    if user_responds.lower() != "yes":
        print(f"I Seee... Enjoy your day, {user_play}")
    else:
        print("Let's begin!!!!")
        start_game(user_responds, user_play)


# Run the script as a main program.
if __name__ == "__main__":
    game()

