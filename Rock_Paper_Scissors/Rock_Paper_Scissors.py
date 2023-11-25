# library module
import random as rand_hand_guesses


choice_mapping_1 = {
    "s": "Scissors",
    "p": "Paper",
    "r": "Rock",
}
# Storing data for user_key input.

choice_mapping_2 = [
    "scissors", "paper", "rock"
]
# Storing data for user_string type input.


def scoreboard(
        user_name, user_wins, computer_name, 
        computer_wins):
    name_header = [
        "Username", "User Wins", 
        "Computer Name", "Computer Wins"
    ]
    score_data = [
        user_name, user_wins, 
        computer_name, computer_wins
    ]

    # Display name header and score together.
    for title, value in zip(name_header, score_data):
        print(f"{title}: {value}")
        pass


def starting_rps():
    print("-------------------------------------------")
    print("| welcome to the rock_paper_scissors game |".title())
    print("-------------------------------------------")

    firstname = input("Enter your firstname : ").lower()
    lastname = input("Enter your lastname : ").lower()
    user_name = " ".join([firstname, lastname])
    # Combine firstname and lastname to the user_name.
    print("Username :", user_name)

    rand_value = 2
    # Declare random number at last index position.
    user_wins = 0
    computer_wins = 0

    while True:
        print("------------------------")
        message_display = ("[--| ✂ Scissors", 
                           " 📜 Paper", 
                           " 🥌 Rock |--]"
                           )
        print(message_display)

        user_choice = input(
            "Option1 : type (s/p/r) | Option2 : type (Scissors/Paper/Rock)\n"
            "Which hand choices would you like to pick?\n"
            " (Scissors[s], Paper[p], Rock[r]): "
        ).lower()

        # First condition checks user key input[s/p/r].
        # Second condition checks user string type input.
        if user_choice in choice_mapping_1:
            user_select = choice_mapping_1[user_choice]
        elif user_choice in choice_mapping_2:
            user_select = user_choice
        else:
            print("Invalid input!")
            continue
            # Continues the loop if user input not matches.

        print("You chose: -->", user_select)
        print("\t##---Next---##")
        break
        # End the control flow loop.

    rand_hand = rand_hand_guesses.randint(0, rand_value)
    # Generates random hand_guesses from 0-2
    computer_pick = choice_mapping_2[rand_hand]
    # Computer using user_string type input.
    computer_name = input("Enter Computer name: ").capitalize()
    print("{} picked --> {}".format(computer_name, computer_pick))
    # Uses string formatting to display concise value.

    if user_select.lower() == "scissors" and computer_pick == "paper":
        print("You have Won!")
        user_wins += 1
    elif user_select.lower() == "paper" and computer_pick == "rock":
        print("You have Won!")
        user_wins += 1
    elif user_select.lower() == "rock" and computer_pick == "scissors":
        print("You have Won!")
        user_wins += 1
    elif user_select.lower() == computer_pick:
        print("Stalemate!")
        user_wins += 0.5
        computer_wins += 0.5
    else:
        print("You have lost!")
        computer_wins += 1

    scoreboard(user_name, user_wins, 
               computer_name, computer_wins
               )
    # Display the scoreboard header.

    # Prompt the user to play again.
    user_play_again = input("Do you want to play again? (y/n):").lower()
    if user_play_again.lower() != "y":
        print("Thank you for your time! Appreciate it😃")
        quit()
        # Exit the program.
    else:
        starting_rps()
        # Reset the program.


# Run the program as a main script.
if __name__ == "__main__":
    starting_rps()


