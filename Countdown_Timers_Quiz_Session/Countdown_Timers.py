import time
import functools


# Define a list of questions with their corresponding answers
questions = [
    ("How many Countries are available in the Asean Market?", "10"),
    ("Who is the Richest Person in the World?", "Elon Musk"),
    ("Who is the Current President of the United Kingdom?", "Penny Mordaunt"),
    ("When did Rainbow Six Siege was official released", "2015"),
    ("Where is Riot Games Headquarter located?", "Los Angeles"),
]


def countdown():
    title = ["Welcome", "To", "The", "Time_Game"]
    title_display = functools.reduce(lambda x, y,: x + " " + y, title)
    print(title_display, "\n")

    fstname = input("Enter your firstname : ").capitalize()
    lstname = input("Enter your lastname : ").capitalize()
    fllname = " ".join([fstname, lstname])
    print("Fullname : ", fllname, "\n")

    user_play = input("Do you want to play? ->(y/n) ").lower()

    if user_play != "y":
        print("Thank you very much!")
        exit()
    else:
        print("Let's play!\n")
        # Continue the game process.

    print("You have to justify the right answers for five questions given?")
    user_play = input(("Countdown begins when you say (yes) :))")).lower()

    if user_play == "yes":
        time_taken = 3
        while time_taken > 0:
            print(f"Time remaining: {time_taken:02d} seconds")
            time.sleep(1)
            time_taken -= 1
        print("countdown begins now!".upper())
    else:
        print("Ahhhh! You miss your opportunity! :(")
        quit()

    player_score = 0

    # Iterate over the questions
    for question, correct_answer in questions:
        answer = input(question)
        if answer.lower() == correct_answer:
            print("You got it right!")
            player_score += 1
        else:
            print("Better luck next time.")

    total_questions = len(questions)
    # Declare new variable of total_questions equal to return length of questions list.
    percentage = (player_score / total_questions) * 100

    print(f"\nYou got {player_score} out of {total_questions} questions correct!")
    print(f"Your score: {percentage}%.")


    user_play_again = input("Do you want to play again? (y/n):").lower()
    if user_play_again.lower() != "y":
        print("Thank you for your time! Appreciate it😃")
        quit()
        # Exit the program.
    else:
        countdown()
        # Reset the program.


if __name__ == "__main__":
    countdown()
