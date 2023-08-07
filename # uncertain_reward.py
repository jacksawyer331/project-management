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


# Create lists for the asnwers
DIF_1_ANSWERS = [7, 3, 9, 3]
DIF_2_ANSWERS = [13, 8, 20, 4]
DIF_3_ANSWERS = [115, 18, 65, 7]
DIF_4_ANSWERS = [515, 183, 2652, 262]
DIF_5_ANSWERS = [4642, 2650, 58368, 382]


# Create a list of difficulties
DIFF_OPTIONS = ["1. Difficulty 1", "2. Difficulty 2", "3. Difficulty 3",
                "4. Difficulty 4", "5. Difficulty 5"]


# Create a menu function
def menu():
    """Display the menu."""
    for i in range(len(DIFF_OPTIONS)):
        print(DIFF_OPTIONS[i])


# print the menu that will the user what difficulty they would like
print("This is a quiz in which you'll be asked questions of a certain "
      "difficulty")
print("")
total_times_used = 0
correct_questions = 0
times_used_1 = 0
times_used_2 = 0
times_used_3 = 0
times_used_4 = 0
times_used_5 = 0
points = 0
question_loop = True
# ask the user which difficulty they would like
while question_loop is True:
    if total_times_used < 20:
        menu()
        underscores()
        user_choice = int(input("Enter a number and press enter: "))
        if user_choice == 1:
            try:
                if times_used_1 < 4:
                    print("You have chosen difficulty 1")
                    underscores()
                    question_1 = (DIF_1_QUESTIONS[times_used_1])
                    answer_1 = int(input("{}: ".format(question_1)))
                    if answer_1 == (DIF_1_ANSWERS[times_used_1]):
                        points += 5
                        times_used_1 += 1
                        total_times_used += 1
                        correct_questions += 1
                        print(
                            "Correct, you have gained 5 points. You have {} "
                            "points"
                            .format(points))
                        underscores()
                    else:
                        times_used_1 += 1
                        total_times_used += 1
                        print(
                            "Incorrect, you have gained 0 points. "
                            "You have {} points"
                            .format(points))
                        underscores()
                elif times_used_1 >= 4:
                    underscores()
                    print("Sorry, there are no more level 1 questions")
                    underscores()
            except ValueError:
                times_used_1 += 1
                total_times_used += 1
                print("Incorrect, you have gained 0 points. You have {} points"
                      .format(points))
                underscores()
                # 2nd difficulty questions
        elif user_choice == 2:
            try:
                if times_used_2 < 4:
                    print("You have chosen difficulty 2")
                    underscores()
                    question_2 = (DIF_2_QUESTIONS[times_used_2])
                    answer_2 = int(input("{}: ".format(question_2)))
                    if answer_2 == (DIF_2_ANSWERS[times_used_2]):
                        points += 10
                        times_used_2 += 1
                        total_times_used += 1
                        correct_questions += 1
                        print(
                            "Correct, you have gained 10 points. You have {} "
                            "points"
                            .format(points))
                        underscores()
                    else:
                        times_used_2 += 1
                        total_times_used += 1
                        print(
                            "Incorrect, you have gained 0 points. "
                            "You have {} points"
                            .format(points))
                        underscores()
                elif times_used_2 >= 4:
                    underscores()
                    print("Sorry, there are no more level 2 questions")
                    underscores()
            except ValueError:
                times_used_2 += 1
                total_times_used += 1
                print("Incorrect, you have gained 0 points. You have {} points"
                      .format(points))
                underscores()
        elif user_choice == 3:
            try:
                if times_used_3 < 4:
                    print("You have chosen difficulty 3")
                    underscores()
                    question_3 = (DIF_3_QUESTIONS[times_used_3])
                    answer_3 = int(input("{}: ".format(question_3)))
                    if answer_3 == (DIF_3_ANSWERS[times_used_3]):
                        points += 15
                        times_used_3 += 1
                        total_times_used += 1
                        correct_questions += 1
                        print(
                            "Correct, you have gained 15 points. You have {} "
                            "points"
                            .format(points))
                        underscores()
                    else:
                        times_used_3 += 1
                        total_times_used += 1
                        print(
                            "Incorrect, you have gained 0 points. "
                            "You have {} points"
                            .format(points))
                        underscores()
                elif times_used_3 >= 4:
                    underscores()
                    print("Sorry, there are no more level 3 questions")
                    underscores()
            except ValueError:
                times_used_3 += 1
                total_times_used += 1
                print("Incorrect, you have gained 0 points. You have {} points"
                      .format(points))
                underscores()
        elif user_choice == 4:
            try:
                if times_used_4 < 4:
                    print("You have chosen difficulty 4")
                    underscores()
                    question_4 = (DIF_4_QUESTIONS[times_used_4])
                    answer_4 = int(input("{}: ".format(question_4)))
                    if answer_4 == (DIF_4_ANSWERS[times_used_4]):
                        points += 20
                        times_used_4 += 1
                        total_times_used += 1
                        correct_questions += 1
                        print(
                            "Correct, you have gained 20 points. You have {} "
                            "points"
                            .format(points))
                        underscores()
                    else:
                        times_used_4 += 1
                        total_times_used += 1
                        print(
                            "Incorrect, you have gained 0 points. "
                            "You have {} points"
                            .format(points))
                        underscores()
                elif times_used_4 >= 4:
                    underscores()
                    print("Sorry, there are no more level 4 questions")
                    underscores()
            except ValueError:
                times_used_4 += 1
                total_times_used += 1
                print("Incorrect, you have gained 0 points. You have {} points"
                      .format(points))
                underscores()
        elif user_choice == 5:
            try:
                if times_used_5 < 4:
                    print("You have chosen difficulty 5")
                    underscores()
                    question_5 = (DIF_5_QUESTIONS[times_used_5])
                    answer_5 = int(input("{}: ".format(question_5)))
                    if answer_5 == (DIF_5_ANSWERS[times_used_5]):
                        points += 25
                        times_used_5 += 1
                        total_times_used += 1
                        correct_questions += 1
                        print(
                            "Correct, you have gained 25 points. You have {} "
                            "points"
                            .format(points))
                        underscores()
                    else:
                        times_used_5 += 1
                        total_times_used += 1
                        print(
                            "Incorrect, you have gained 0 points. "
                            "You have {} points"
                            .format(points))
                        underscores()
                elif times_used_5 >= 4:
                    underscores()
                    print("Sorry, there are no more level 5 questions")
                    underscores()
            except ValueError:
                times_used_5 += 1
                total_times_used += 1
                print("Incorrect, you have gained 0 points. You have {} points"
                      .format(points))
                underscores()
        else:
            print("Please enter a valid option")
    elif total_times_used >= 20:
        question_loop = False
        print("You have answered all questions in this quiz.")
        print("You answered {}/20 questions correctly ".format
              (correct_questions))
        print("You ended with {} points".format(points))
