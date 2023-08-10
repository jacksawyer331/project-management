# uncertain_reward.py
# Author: Jack
# 21/06/23
import time


def underscores():
    """Print underscores."""
    print("")
    print("_" * 35)
    print("")


def linebreak():
    """print linebreak."""
    print("-" * 70)


# Create a list of questions
DIF_1_QUESTIONS = ["5 + 2", "9 - 6", "3 x 3", "9 / 3"]
DIF_2_QUESTIONS = ["7 + 6", "15 - 7", "4 x 5", "12 / 3"]
DIF_3_QUESTIONS = ["76 + 39", "45 - 27", "13 x 5", "42 / 6"]
DIF_4_QUESTIONS = ["136 + 379", "769 - 586", "78 x 34", "786 / 3"]
DIF_5_QUESTIONS = ["1075 + 3567", "6547 - 3897", "152 x 384", "3056 / 8"]


# Create a list of bonus questions
DIF_1_BONUS = ["7 + 9", "18 - 9", "6 x 3", "16 / 4"]
DIF_2_BONUS = ["58 + 45", "72 - 29", "15 x 4", "64 / 8"]
DIF_3_BONUS = ["275 + 567", "859 - 375", "56 x 65", "844 / 4"]
DIF_4_BONUS = ["2768 + 5687", "9485 - 3846", "784 x 323", "4568 / 8"]
DIF_5_BONUS = ["84654 + 47845", "74855 - 65343", "1024 x 6573", "55642 / 2"]

# Create lists for the answers
DIF_1_ANSWERS = [7, 3, 9, 3]
DIF_2_ANSWERS = [13, 8, 20, 4]
DIF_3_ANSWERS = [115, 18, 65, 7]
DIF_4_ANSWERS = [515, 183, 2652, 262]
DIF_5_ANSWERS = [4642, 2650, 58368, 382]


# Create a list of asnwwers for the bonus question
BONUS_1_ANSWERS = [16, 9, 18, 4]
BONUS_2_ANSWERS = [103, 43, 60, 8]
BONUS_3_ANSWERS = [842, 484, 3640, 211]
BONUS_4_ANSWERS = [8455, 5639, 253232, 571]
BONUS_5_ANSWERS = [132499, 9512, 6730752, 27821]


# Create a list of difficulties
DIFF_OPTIONS = ["1. Difficulty 1", "2. Difficulty 2", "3. Difficulty 3",
                "4. Difficulty 4", "5. Difficulty 5", "6. Quit"]


# Create a menu function
def menu():
    """Display the menu."""
    for i in range(len(DIFF_OPTIONS)):
        print(DIFF_OPTIONS[i])


# print the menu that will the user what difficulty they would like
print("This is a quiz in which you'll be asked questions of a certain "
      "difficulty")
linebreak()
print("If you answer the question correctly you wil be given "
      "the option to answer a bonus question")
linebreak()
print("If you answer the bonus question correctly, you will earn bonus points")
linebreak()
print("However, if you answer incorrectly, you will be deducted points")
underscores()
time.sleep(5)
total_times_used = 0
correct_questions = 0
correct_bonus = 0
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
        try:
            user_choice = int(input("Enter a number and press enter: "))
            if user_choice == 1:
                try:
                    # ask the user a levl 1 question
                    if times_used_1 < 4:
                        print("You have chosen difficulty 1")
                        underscores()
                        question_1 = (DIF_1_QUESTIONS[times_used_1])
                        answer_1 = int(input("{}: ".format(question_1)))
                        if answer_1 == (DIF_1_ANSWERS[times_used_1]):
                            points += 5
                            correct_questions += 1
                            print(
                                "Correct, you have gained 5 points. "
                                "You have {} points"
                                .format(points))
                            underscores()
                            # ask the user if they would like to answer a
                            # bonus question
                            bonus_1 = input("Would you like to answer a bonus "
                                            "question for a chance "
                                            "at extra points? (y/n): ")
                            try:
                                if bonus_1 == "y" or bonus_1 == "Y":
                                    underscores()
                                    b_question_1 = (DIF_1_BONUS[
                                        times_used_1])
                                    bonus_1_answer = int(input("{}: "
                                                               .format
                                                               (b_question_1)))
                                    # give the user the correct amount of
                                    # points if they get the answer correct
                                    if bonus_1_answer == (BONUS_1_ANSWERS
                                                          [times_used_1]):
                                        points += 10
                                        correct_bonus += 1
                                        print("Correct, you have gained "
                                              "an extra "
                                              "10 points. You have {} points"
                                              .format(points))
                                        underscores()
                                        times_used_1 += 1
                                        total_times_used += 1
                                    else:
                                        # remove points if the user got the
                                        # answer wrong
                                        times_used_1 += 1
                                        total_times_used += 1
                                        points -= 5
                                        print(
                                            "Incorrect, you have lost 5 "
                                            "points. "
                                            "You have {} points"
                                            .format(points))
                                        underscores()
                                else:
                                    underscores()
                                    times_used_1 += 1
                                    total_times_used += 1
                            except ValueError:
                                times_used_1 += 1
                                total_times_used += 1
                                points -= 5
                                print(
                                    "Incorrect, you have lost 5 "
                                    "points. "
                                    "You have {} points"
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
                    print("Incorrect, you have gained 0 points. "
                          "You have {} points"
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
                            correct_questions += 1
                            print(
                                "Correct, you have gained 10 points. "
                                "You have {} points"
                                .format(points))
                            underscores()
                            # level 2 bonus question
                            bonus_2 = input("Would you like to answer a "
                                            "bonus question for a chance "
                                            "at extra points? (y/n): ")
                            try:
                                if bonus_2 == "y" or bonus_2 == "Y":
                                    underscores()
                                    b_question_2 = (DIF_2_BONUS[
                                        times_used_2])
                                    bonus_2_answer = int(input("{}: "
                                                               .format
                                                               (b_question_2)))
                                    if bonus_2_answer == (BONUS_2_ANSWERS
                                                          [times_used_2]):
                                        points += 20
                                        correct_bonus += 1
                                        print("Correct, you have gained "
                                              "an extra "
                                              "20 points. You have {} points"
                                              .format(points))
                                        underscores()
                                        times_used_2 += 1
                                        total_times_used += 1
                                    else:
                                        times_used_2 += 1
                                        total_times_used += 1
                                        points -= 10
                                        print(
                                            "Incorrect, you have lost 10 "
                                            "points. "
                                            "You have {} points"
                                            .format(points))
                                        underscores()
                                else:
                                    underscores()
                                    times_used_2 += 1
                                    total_times_used += 1
                            except ValueError:
                                times_used_2 += 1
                                total_times_used += 1
                                points -= 10
                                print(
                                    "Incorrect, you have lost 10 "
                                    "points. "
                                    "You have {} points"
                                    .format(points))
                                underscores()
                        else:
                            underscores()
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
                    print("Incorrect, you have gained 0 points. "
                          "You have {} points"
                          .format(points))
                    underscores()
            elif user_choice == 3:
                try:
                    # 3rd question
                    if times_used_3 < 4:
                        print("You have chosen difficulty 3")
                        underscores()
                        question_3 = (DIF_3_QUESTIONS[times_used_3])
                        answer_3 = int(input("{}: ".format(question_3)))
                        if answer_3 == (DIF_3_ANSWERS[times_used_3]):
                            points += 15
                            correct_questions += 1
                            print(
                                "Correct, you have gained 15 points. "
                                "You have {} points"
                                .format(points))
                            underscores()
                            # level 3 bonus question
                            bonus_3 = input("Would you like to answer a bonus "
                                            "question for a chance "
                                            "at extra points? (y/n): ")
                            try:
                                if bonus_3 == "y" or bonus_3 == "Y":
                                    underscores()
                                    b_question_3 = (DIF_3_BONUS[
                                        times_used_3])
                                    bonus_3_answer = int(input("{}: "
                                                               .format
                                                               (b_question_3)))
                                    if bonus_3_answer == (BONUS_3_ANSWERS
                                                          [times_used_3]):
                                        points += 30
                                        correct_bonus += 1
                                        print("Correct, you have gained "
                                              "an extra "
                                              "30 points. You have {} points"
                                              .format(points))
                                        underscores()
                                        times_used_3 += 1
                                        total_times_used += 1
                                    else:
                                        times_used_3 += 1
                                        total_times_used += 1
                                        points -= 15
                                        print(
                                            "Incorrect, you have lost 15 "
                                            "points. "
                                            "You have {} points"
                                            .format(points))
                                        underscores()
                                else:
                                    underscores()
                                    times_used_3 += 1
                                    total_times_used += 1
                            except ValueError:
                                times_used_3 += 1
                                total_times_used += 1
                                points -= 15
                                print(
                                    "Incorrect, you have lost 15 "
                                    "points. "
                                    "You have {} points"
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
                    print("Incorrect, you have gained 0 points. "
                          "You have {} points"
                          .format(points))
                    underscores()
            elif user_choice == 4:
                try:
                    # level 4 questions
                    if times_used_4 < 4:
                        print("You have chosen difficulty 4")
                        underscores()
                        question_4 = (DIF_4_QUESTIONS[times_used_4])
                        answer_4 = int(input("{}: ".format(question_4)))
                        if answer_4 == (DIF_4_ANSWERS[times_used_4]):
                            points += 20
                            correct_questions += 1
                            print(
                                "Correct, you have gained 20 points. "
                                "You have {} points"
                                .format(points))
                            underscores()
                            # level 4 bonus questions
                            bonus_4 = input("Would you like to answer a bonus "
                                            "question for a chance "
                                            "at extra points? (y/n): ")
                            try:
                                if bonus_4 == "y" or bonus_4 == "Y":
                                    underscores()
                                    b_question_4 = (DIF_4_BONUS[
                                        times_used_4])
                                    bonus_4_answer = int(input("{}: "
                                                               .format
                                                               (b_question_4)))
                                    if bonus_4_answer == (BONUS_4_ANSWERS
                                                          [times_used_4]):
                                        points += 40
                                        correct_bonus += 1
                                        print("Correct, you have gained "
                                              "an extra "
                                              "40 points. You have {} points"
                                              .format(points))
                                        underscores()
                                        times_used_4 += 1
                                        total_times_used += 1
                                    else:
                                        times_used_4 += 1
                                        total_times_used += 1
                                        points -= 20
                                        print(
                                            "Incorrect, you have lost 20 "
                                            "points. "
                                            "You have {} points"
                                            .format(points))
                                        underscores()
                                else:
                                    underscores()
                                    times_used_4 += 1
                                    total_times_used += 1
                            except ValueError:
                                times_used_4 += 1
                                total_times_used += 1
                                points -= 20
                                print(
                                    "Incorrect, you have lost 20 "
                                    "points. "
                                    "You have {} points"
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
                    print("Incorrect, you have gained 0 points. "
                          "You have {} points"
                          .format(points))
                    underscores()
            elif user_choice == 5:
                # level 5 questions
                try:
                    if times_used_5 < 4:
                        print("You have chosen difficulty 5")
                        underscores()
                        question_5 = (DIF_5_QUESTIONS[times_used_5])
                        answer_5 = int(input("{}: ".format(question_5)))
                        if answer_5 == (DIF_5_ANSWERS[times_used_5]):
                            points += 25
                            correct_questions += 1
                            print(
                                "Correct, you have gained 25 points. "
                                "You have {} points"
                                .format(points))
                            underscores()
                            # level 5 bonus questions
                            bonus_5 = input("Would you like to answer a bonus "
                                            "question for a chance "
                                            "at extra points? (y/n): ")
                            try:
                                if bonus_5 == "y" or bonus_5 == "Y":
                                    underscores()
                                    b_question_5 = (DIF_5_BONUS[
                                        times_used_5])
                                    bonus_5_answer = int(input("{}: "
                                                               .format
                                                               (b_question_5)))
                                    if bonus_5_answer == (BONUS_5_ANSWERS
                                                          [times_used_5]):
                                        points += 50
                                        correct_bonus += 1
                                        print("Correct, you have gained "
                                              "an extra "
                                              "50 points. You have {} points"
                                              .format(points))
                                        underscores()
                                        times_used_5 += 1
                                        total_times_used += 1
                                    else:
                                        times_used_5 += 1
                                        total_times_used += 1
                                        points -= 25
                                        print(
                                            "Incorrect, you have lost 25 "
                                            "points. "
                                            "You have {} points"
                                            .format(points))
                                        underscores()
                                else:
                                    underscores()
                                    times_used_5 += 1
                                    total_times_used += 1
                            except ValueError:
                                times_used_5 += 1
                                total_times_used += 1
                                points -= 25
                                print(
                                    "Incorrect, you have lost 25 "
                                    "points. "
                                    "You have {} points"
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
                    print("Incorrect, you have gained 0 points. "
                          "You have {} points"
                          .format(points))
                    underscores()
            elif user_choice == 6:
                question_loop = False
                print("You answered {}/20 questions correctly".format
                      (correct_questions))
                print("You answered {}/20 bonus questions correctly"
                      .format(correct_bonus))
                print("You ended with {} points".format(points))
                print("Thank you for playing!")
            else:
                print()
                print("Please enter a valid option")
                underscores()
        except ValueError:
            print()
            print("Please enter a valid option")
            underscores()
    elif total_times_used >= 20:
        question_loop = False
        print("You have answered all questions in this quiz.")
        print("You answered {}/20 questions correctly".format
              (correct_questions))
        print("You answered {}/20 bonus questions correctly"
              .format(correct_bonus))
        print("You ended with {} points".format(points))
        print("Thank you for playing!")
