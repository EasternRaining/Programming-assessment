import math
import random
from zipfile import error


# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")


def instruction():
    print('''

**** Instructions ****

To begin the quiz, choose the number of questions

Then choose how many questions you'd like to play <enter> for 
infinite mode.

Your goal is to get as much of these basic maths questions
right as possible

 Good luck.   

    ''')

# checks for an integer with optional upper /
# lower limits and an optional exit code for infinite mode
# / quitting the game
def int_check(question, low=None, high=None, exit_code=None):
    # if any integer is allowed...
    if low is None and high is None:
        error = "Please enter an integer"

    # if the number needs to be more than an
    # integer (ie: rounds / 'high number')
    elif low is not None and high is None:
        error = (f"Please enter an integer that is "
                 f"more than / equal to {low}")

    # if the number needs to between low & high
    else:
        error = (f"Please enter an integer that"
                 f" is between {low} and {high} (inclusive)")

    while True:
        response = input(question).lower()

        # check for infinite mode / exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            # Check the integer is not too low...
            if low is not None and response < low:
                print(error)

            # check response is more than the low number
            elif high is not None and response > high:
                print(error)

            # if the response is valid, return it
            else:
                return response

        except ValueError:
            print(error)


def answer_compare(user, comp):

    # If the user and the computer choice is the same, it's a lie
    if user == comp:
        round_result = "win"

    # if it's not a win / tie, then it's a loss
    else:
        round_result = "lose"

    return round_result

# list of all the "basic" math questions that are going to be played
Questions_list = []



# Initialise quiz variables
mode = "regular"
questions_played = 0
end_quiz = "no"
feedback = ""



quiz_history = []
all_scores = []

# Starting the quiz
print("️➕➖ Welcome to the Basic Math Quiz ➗✖️")
print()

want_instructions = yes_no("Do you want to read instructions? ")

# Checks if user wants to play or not (y) yes, (n) no
if want_instructions == "yes":
    instruction()

# Ask user for number of questions / infinite mode
num_questions = int_check(question="Rounds <enter for infinite>: ",
                       low=1, exit_code="")

if num_questions == "":
    mode = "infinite"
    num_questions = 99

# Game starts here
while questions_played < num_questions:

    # Rounds headings
    if mode == "infinite":
        rounds_heading = f"\n♾️♾️ Round {questions_played + 1} (Infinite Mode) ♾️♾️"
    else:
        rounds_heading = f"\n➕➖ Round {questions_played + 1} of {num_questions} ➗✖️"

    print(rounds_heading)
    print()

    # randomly choose from questions list (remove the [:-1] if needed)
    comp_choice = random.choice(Questions_list[:-1])
    print("Computer choice", comp_choice)

    # Questions start here
    # set the guesses to 0 at the start of every round
    questions_answered = 0
    already_answered = []


    # get user answer
    user_answer = ("Choose: ", Questions_list)
    print("you chose", user_answer)

    result = answer_compare(user_answer, comp_choice)

    # check that they don't want to quit
    if user_answer == "xxx":
        # set end_game to use so that outer loop can be broken
        end_quiz = "yes"
        break

    # once you answer a question add +1 to total questions answered
    questions_answered += 1


    # Rounds end here

    # if user has entered exit code, end game!!
    if end_quiz == "yes":
        break

    questions_played += 1

    # Add round result to game history
    history_feedback = f"Round {questions_played}: {feedback}"
    quiz_history.append(history_feedback)

    # add guesses used to score list
    all_scores.append(questions_answered)

    # if users are in infinite mode, increase number of questions by +1
    if mode == "infinite":
        num_questions += 1

# Quiz ends here

# Before calculating statistics:
if questions_played > 0:
    # History / Statistics area



    # ask the user if they want to see their quiz history
    see_history = yes_no("\nDo you want to see your quiz history? ")
    if see_history == "yes":
        for item in quiz_history:
            print(item)

    print()
    print("Thanks for playing.")

else:
    print("Ight, thanks for playing.")