# The following are some test strings to pass in to the play_game function.
easy_quiz = ["Batman's real name is ___ Wayne"]
answer_easy = ['Bruce']

medium_quiz = ["___ is a natural phenomenon by which all things with mass are brought toward one another, including planets, stars and galaxies, and other physical objects."]
answer_medium = ['Gravity']

hard_quiz = ["The ___ constant is a physical constant that is the quantum of action, central in quantum mechanics"]
answer_hard = ['Plank']

from time import sleep
from random import randint
#Using the following function to choose the level of difficulties of the quizs
def choose_difficulty():
    user_input = None
    while user_input not in [1,2,3]:
        user_input = raw_input("Select 1 for easy, select 2 for medium, select 3 for hard: ")
        if user_input == "1":
            print "easy mode selected"
            return "easy"
        elif user_input == "2":
            print "medium mode selected"
            return "medium"
        elif user_input == "3":
            print "hard mode selected"
            return "hard"
        else:
            print "Invaild input, please type in numbers and do it again"

#start quiz by choosing difficulty and answer the question
def quiz_start():
    difficulty = choose_difficulty()
    if difficulty =="easy":
        for i in range(len(easy_quiz)):
            user_input = raw_input(easy_quiz[i] + "\nYour answer: ")
            if user_input.lower() == answer_easy[i].lower():
                print "Congrats! "+ easy_quiz[i].replace("___",answer_easy[i])
            else:
                print "You are wrong!"

    if difficulty =="medium":
        for i in range(len(medium_quiz)):
            user_input = raw_input(medium_quiz[i] + "\nYour answer: ")
            if user_input.lower() == answer_medium[i].lower():
                print "Congrats! "+ medium_quiz[i].replace("___",answer_medium[i])
            else:
                print "You are wrong!"

    if difficulty =="hard":
        for i in range(len(easy_quiz)):
            user_input = raw_input(hard_quiz[i] + "\nYour answer: ")
            if user_input.lower() == answer_hard[i].lower():
                print "Congrats! "+ hard_quiz[i].replace("___",answer_hard[i])
            else:
                print "You are wrong!"

quiz_start()
