# The following are some test strings to pass in to the play_game function.
easy_quiz = "Batman's real name is ___ ___. Superman's real name is ___ ___"
answer_easy = ['Bruce','Wayne','Clark','Kent']

medium_quiz = "___ is a natural phenomenon by which all things with ___ are brought toward one another, including ___, ___ and galaxies, and other physical objects."
answer_medium = ['Gravity','mass','planets','stars']

hard_quiz = "The ___ ___ is a physical constant that is the quantum of action, central in ___ ___"
answer_hard = ['Plank','constant','quantum','mechanics']

from time import sleep
from random import randint
#Using the following function to choose the level of difficulties of the quizs and start doing your quiz
def do_quiz():
    user_input = None
    while user_input not in [1,2,3]:
        user_input = raw_input("Select 1 for easy, select 2 for medium, select 3 for hard: ")
        if user_input == "1":
            print "easy mode selected"
            return quiz_start(easy_quiz,answer_easy)
        elif user_input == "2":
            print "medium mode selected"
            return quiz_start(medium_quiz,answer_medium)
        elif user_input == "3":
            print "hard mode selected"
            return quiz_start(hard_quiz,answer_hard)
        else:
            print "Invaild input, please type in numbers and do it again"

#start quiz by choosing difficulty and answer the question
def quiz_start(quiz,answer):
    user_input = raw_input("Your answer(please seperate each word with a space): ").split()
    user_answer = quiz
    while [x.lower() for x in user_input] != [x.lower() for x in answer]:
        print "You are wrong! do it again"
        user_input = raw_input("Your answer(please seperate each word with a space): ").split()
    for i in range(len(answer)):
        user_answer = user_answer.replace("___",answer[i],1)
    print "Congrats, "+ user_answer
do_quiz()
