
# Dice Guesser🎲

Welcome to the Dice Guesser, a simple Python command-line where shows you on guessing the dice throw with your expectation.

1. **How to Play:**
   - Enter your dear name.
   - Guess the dice.
   - Result will be shown.
   -  If you guessed correctly, congratulations. Otherwise, try again and hope for better luck!!

2. **Features:**
   - The game can be played multiple times.
   - Option to exit the game at any time.
   - User-friendly prompts and game approachment.

3. **Problem Observation:**
   *Code Syntax* 
   try:
        user_guess = int(input("Make a guess (1-6): "))
        dice_roll = roll_dice()

        if user_guess != dice_roll:
            print(f"You got it wrong. The dice rolled {dice_roll}")
        elif user_guess < dice_roll or user_guess > dice_roll:
            print("Invalid input. Please enter a number between 1 and 6.")
        else:
            print("You got it right!")
            dice_guesses += 1
                
    except ValueError:
        print("No names input.")
        continue

*Explanation:*
- I observe that logic flow on *elif condition user_guess < dice_roll or user_guess > dice_roll* should be unnecessary since *user_guess != dice_roll* has been executed to check the condition matches and return True if condition is fit in.
----------------------------------------------------------------
4. **Solution Approach:**
- Instead of using *'elif'* statement, declare if statement below *user_guess* input statement to run the logic flow without any error or bug detected.

*Code Syntax*
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
----------------------------------------------------------------------------------------------
## Usage 

1. Execute the script by running 'Dice_Guesser.py'

2. Follow the on-screen instructions to play the game.

Enjoy playing the Well-Known Dice Game🎲, Ciao🤨






