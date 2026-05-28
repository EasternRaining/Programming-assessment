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

To begin, please choose the number of questions you'd like
and press <enter> for infinite questions.

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
    basicfacts = ['+','-','*','/']
    comp = random.choice(basicfacts)

    # addition, simple use random randint to generate random numbers from
    # 1 to 100 which we will then add together
    if comp == "+":
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        answer = num1 + num2
        question = f" {num1} + {num2} = "

    # subtraction, slightly more complicated, but we will subtract the number
    elif comp == "-":
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        # if the 2nd number is greater than the 1st number
        # this is to prevent negatives from happening
        if num2 > num1:
            num1, num2 = num2, num1
        answer = num1 - num2
        question = f" {num1} - {num2} = "


    # multiplication, also pretty simple, just generate a number from 1 to 12 to multiply together
    elif comp == "*":
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        answer = num1 * num2
        question = f" {num1} * {num2} = "

    else: # division
        # since division is linked with multiplication, I used multiplication
        # to multiply the 2nd number with the answer to get the 1st number
        # this is foolproof since all the questions and answers are directly linked to each other
        # this works because only whole numbered division questions are used making it easier for the user to answer
        answer = random.randint(1, 12)
        num2 = random.randint(1, 12)
        num1 = num2 * answer
        question = f" {num1} divided by {num2} = "

    # used to retrieve the answer from the question
    return question, answer

# will be used as part of the question generation formula later on
def get_user_answer(question):

    while True:
        response = input(question).lower()
        # user can type in exit code during question to end the quiz
        if response.lower() == "xxx":
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
num_questions = int_check(question="How much Questions do you want?, <enter> for infinite: ",
                       low=1, exit_code="")

# for infinite mode
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

    # Questions start here, this formula generates the users question, and already prepares the answer
    question, correct_answer = basic_facts()

    # Get the users answer, this formula receives the users answer
    # by using the get_user_answer function
    user_answer = get_user_answer(question)

    # check that they don't want to quit. if the user quits, then break the game
    if user_answer == "xxx":
        # set end_quiz to yes so that the loop can be broken
        end_quiz = "yes"
        break


    # if a user answers a question, call back to the correct answer formula
    if user_answer == correct_answer:
        print("✅ Correct!")
        # feedback and right answer are for history purposes later on
        # use f" to be able to record the users answer
        feedback = f"✅ Correct! {user_answer}"
        right_answer += 1
    # if the answer is anything but the correct answer, make it an incorrect answer
    else:
        print("❌ Incorrect!")
        # feedback and wrong answer are for history purposes later on
        # use f" to be able to show the question that they answered incorrectly,
        # display the actual correct answers and record the users answer right next to it
        feedback = f"❌ Incorrect! {question}{correct_answer}, Not {user_answer}"
        wrong_answer += 1

    # Rounds end here

    # if user has entered exit code, end game!!
    if end_quiz == "yes":
        break

    questions_played += 1

    # Add round result to game history (taken from HL)
    # just swapped the variables around to match the math quiz's variables
    history_feedback = f"Round {questions_played}: {feedback}"
    quiz_history.append(history_feedback)


    # add guesses used to score list
    all_scores.append(user_answer)

    # if users are in infinite mode, increase number of rounds
    if mode == "infinite":
        num_questions += 1


    """ The Quiz """




    """ The History """

if questions_played > 0:
    # Calculate statistics
    answered_right = right_answer / questions_played * 100
    answered_wrong = wrong_answer / questions_played * 100


    # Output Game Statistics
    print("📊📊📊 Quiz Statistics 📊📊📊")
    print(f"👍 Correct: {answered_right:.2f}% \t "
          f"😢 Incorrect: {answered_wrong:.2f}% \t ")

    # ask the user if they want to see their quiz history and output if requested.
    see_history = yes_no("\nDo you want to see your quiz history? ")
    if see_history == "yes":
        for item in quiz_history:
            print(item)

    print()
    print("Thanks for playing.")

else:
    print("Ight, Thanks for playing.")


    """ The History """

# end of the quiz