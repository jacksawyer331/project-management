# uncertain_reward.py
# Author: Jack
# 21/06/23
import random


def underscores():
    """Print underscores."""
    print("")
    print("_" * 35)
    print("")


# Create a list of possible questions
DIF_1_QUESTIONS = ["5 + 2", "9 - 6", "3 x 3", "9 / 3"]
DIF_2_QUESTIONS = ["7 + 6", "15 - 7", "4 x 5", "12 / 3"]
DIF_3_QUESTIONS = ["76 + 39", "45 - 27", "13 x 5", "42 / 6"]
DIF_4_QUESTIONS = ["136 + 379", "769 - 586", "78 x 34", "786 / 3"]
DIF_5_QUESTIONS = ["1075 + 3567", "6547 - 3897", "152 x 384", "3056 / 8"]

# Create a list of difficulties
DIFF_OPTIONS = ["1. Difficulty 1", "2. Difficulty 2", "3. Difficulty 3",
                "4. Difficulty 4", "5. Difficulty 5"]


# Create a menu function
def menu():
    """Display the menu."""
    for i in range(len(DIFF_OPTIONS)):
        print(DIFF_OPTIONS[i])


# print the menu that will the user what difficulty they would like
print("Welcome to the game where you never know what you're going to get")
menu()
underscores()
# ask the user which difficulty they would like
user_choice = int(input("Enter a number and press enter: "))
if user_choice == 1:
    print("You have chosen difficulty 1")
    underscores()
    question_1 = random.choice(DIF_1_QUESTIONS)
    answer_1 = int(input("{}: ".format(question_1)))
elif user_choice == 2:
    print("You have chosen difficulty 2")
    underscores()
    question_2 = random.choice(DIF_2_QUESTIONS)
    answer_2 = int(input("{}: ".format(question_2)))
elif user_choice == 3:
    print("You have chosen difficulty 3")
    underscores()
    question_3 = random.choice(DIF_3_QUESTIONS)
    answer_3 = int(input("{}: ".format(question_3)))
elif user_choice == 4:
    print("You have chosen difficulty 4")
    underscores()
    question_4 = random.choice(DIF_4_QUESTIONS)
    answer_4 = int(input("{}: ".format(question_4)))
elif user_choice == 5:
    print("You have chosen difficulty 5")
    underscores()
    question_5 = random.choice(DIF_5_QUESTIONS)
    answer_5 = int(input("{}: ".format(question_5)))
