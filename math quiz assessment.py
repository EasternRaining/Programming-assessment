import math
import random

""" Quiz Functions """


# Check that users have entered a valid
# option based on a list
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


# Displays instructions

def instruction():
    print('''

**** Instructions ****

Welcome to the Basic Math Quiz

To begin, please choose the number of rounds you'd like
and press <enter> for infinite rounds.

Then the computer will generate a math quiz based on
addition, subtraction, or multiplication, then it's your job
to answer these math questions correctly.

Press <xxx> to exit the quiz at any time

Then your results will be displayed to show you how well you scored

Good luck!

    ''')


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



def basic_facts():
    """ outlines the math questions we are going to do"""
    basicfacts = ['+','-','*']
    comp = random.choice(basicfacts)

    # addition, simple use random randint to generate random numbers from
    # 1 to 100 which we will then add together
    if comp == "+":
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        answer = num1 + num2
        question = f" {num1} + {num2}"

    # subtraction, slightly more complicated, but we will subtract the number
    elif comp == "-":
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        # if the 2nd number is greater than the 1st number
        if num2 > num1:
            num1, num2 = num2, num1
        answer = num1 - num2
        question = f" {num1} - {num2}"


    # multiplication, also pretty simple, just generate a number from 1 to 12 to multiply and add
    else:
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        answer = num1 * num2
        question = f" {num1} * {num2}"


# will be used as part of the question generation formula later on
def get_user_answer(question):

    while True:
        response = input(question).lower()
        # user can type in exit code during question to end the quiz
        if response == "xxx":
            return "xxx"
        # only whole numbers are accepted
        try:
            return int(response)
        except ValueError:
            print("Please enter enter in a whole number please")





""" Quiz Functions """



""" The Quiz """


# Initialise quiz variables
mode = "regular"
questions_played = 0
end_quiz = "no"
feedback = ""
# for history needs later on
right_answer = 0
wrong_answer = 0

quiz_history = []
all_scores = []

print("➕✖️ Welcome to the Basic Math Quiz ➖➕")
print()

# lets the user know if they want instructions
want_instructions = yes_no("Do you want to read the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()


# Ask user for number of rounds / infinite mode
num_questions = int_check(question="Rounds <enter for infinite>: ",
                       low=1, exit_code="xxx")

if num_questions == "":
    mode = "infinite"
    num_questions = 99

# Game loop starts here
while questions_played < num_questions:

    # Rounds headings
    if mode == "infinite":
        rounds_heading = f"\n♾️♾️️ Round {questions_played + 1} (Infinite Mode) ♾️♾️"
    else:
        rounds_heading = f"\n➕✖️ Round {questions_played + 1} of {num_questions} ➖➕"

    print(rounds_heading)
    print()






    """ The History """



if questions_played > 0:
    # Calculate statistics
    rounds_won = rounds_played  rounds_lost
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100

    # Output Game Statistics
    print("📊📊📊 Game Statistics 📊📊📊")
    print(f"👍 Won: {percent_won:.2f} \t "
          f"😢 Lost: {percent_lost:.2f} \t "
          f"👔 Tied: {percent_tied:,2f}")

    # ask the user if they want to see their game history and output if requested.
    see_history = string_checker("\nDo you want to see your game history? ")
    if see_history == "yes":
        for item in game_history:
            print(item)

    print()
    print("Thanks for playing.")

else:
    print("🐔🐔🐔 Oops - You chickened out! 🐔🐔🐔")