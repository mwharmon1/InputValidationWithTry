""" Author: Michael Harmon
    Last Date Modified: 09/23/2019
    Description: This program will prompt for user's name
    and 3 scores out of 100 then average the scores and
    display the name and average grade.
    Update: Wrapped the average function call around a try except block.
    Updated: moved user input of try block.
"""


def average(score1, score2, score3):
    if score1 <= 0 or score2 <= 0 or score3 <= 0:
        raise ValueError
    else:
        average_score = (float(score1) + float(score2) + float(score3)) / 3
        return average_score


if __name__ == '__main__':
    last_name = input('Enter your last name. ')
    first_name = input('Enter your first name. ')
    age = input('Enter your age. ')
    score_1 = int(input('Enter 1st score out of 100: '))
    score_2 = int(input('Enter 2nd score out of 100: '))
    score_3 = int(input('Enter 3rd score out of 100: '))
    try:
        average_scores = average(score_1, score_2, score_3)
    except ValueError:
        print("No negative scores please.")
    else:
        print(last_name + ', ' + first_name + ' age ' + age + ' average grade:' '% 5.2f' % average_scores)
