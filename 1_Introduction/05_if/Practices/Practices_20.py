"""
Create a simple game to ask 5 questions to the user and show a summary with how many right answers the user had.
"""
question1 = 'Question 1: '
question2 = 'Question 2: '
question3 = 'Question 3: '
question4 = 'Question 4: '
question5 = 'Question 5: '

answer1 = 'Answer 1'
answer2 = 'Answer 2'
answer3 = 'Answer 3'
answer4 = 'Answer 4'
answer5 = 'Answer 5'

user_answer1 = input(question1)
user_answer2 = input(question2)
user_answer3 = input(question3)
user_answer4 = input(question4)
user_answer5 = input(question5)

correct_answers = 0
if answer1 == user_answer1:
    correct_answers += 1
if answer2 == user_answer2:
    correct_answers += 1
if answer3 == user_answer3:
    correct_answers += 1
if answer4 == user_answer4:
    correct_answers += 1
if answer5 == user_answer5:
    correct_answers += 1

if correct_answers == 0:
    print("Sorry but you had no correct answer")
else:
    print("You had {0} correct answer(s)".format(correct_answers))

