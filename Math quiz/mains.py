# This is my whole code
import random
# This shows what types of maths in uses
all_question_types = ["+", "-", "x", "/"]
# This shows how far the numbers will go in the questions
score = 0
first_number = random.randrange(1, 20)
second_number = random.randrange(1, 20)
# This shows the questions and the amount of questions
question_number = 0
question_count = 0
final_question_count = 0
# This shows if they put an invalid answer
def int_checker(question):
    while True:
        try:
            return int(input(question))
        except:
            print("Put a valid numbah Bruh")


def one_question():
    global question_types, score
    question_types = random.choice(all_question_types)
    first_number = random.randrange(1, 20)
    second_number = random.randrange(1, 20)
    correct_answer = 0.0
# This shows it can do addition
    if question_types == "+":
        correct_answer = first_number + second_number
# This shows it can do subtraction
    elif question_types == "-":
        correct_answer = first_number - second_number
# This shows it can do Times table
    elif question_types == "x":
        correct_answer = first_number * second_number
# This shows it can do Division
    elif question_types == "/":
        correct_answer = first_number / second_number
    correct_answer = round(correct_answer, 1)
    question = "What is {} {} {}? (rounded to the first decimal place)\n".format(first_number, question_types,
                                                                                 second_number)
    user_answer = float(input(question))
    user_answer = round(user_answer, 1)
    if user_answer == round(correct_answer, 1):
        print("Fah your smart!")
        score += 1
    else:
        print(f"Incorrect! HAHA! {correct_answer}")
# Displays when your asked if you want to start
def main():
    global question_number, question_count, final_question_count
    while True:
        game = input("Chur ready Chuz? (Y/N)\n").capitalize()
        if game == "Yes" or game == "Y":
            question_count = question_number + int_checker("How many questions mistah driftah?\n")
            final_question_count += question_count
            print("Lets a go")
            break
# This shows what they'll get if they say n
        elif game == "No" or game == "N":
            print("Too Bad monkey your playing")
# This shows what it'll say if they put m
        elif game == "Maybe":
            print("pick one already ya taking all day!")
# This shows if they put no valid answer
        else:
            print("Put a valid answer or ill be really sad")


    for question_number in range(question_count):
        print(f"Question {question_number + 1}")
        one_question()
# Displayed when the code starts
print("% ~x~x~x~x~  % Math Quiz %  ~x~x~x~x~ %")
username = input("Enter ya name already bro we burning daylight\n").capitalize()
print("Welcome to the game {}".format(username))
# Displays when the codes finished
main()
print("Yeah go away now bro")