"""
Read the name, frequency (%) and the numbers of correct answers (0..25) of a student and print his name and
Grade based on the table below:
0 to 10 questions = Grade D
11 to 15 questions = Grade C
16 to 20 questions = Grade B
21 to 25 questions = Grade A
Obs: If the student has less than 75% of frequency his Grade should be Failed.
"""

name = input("Name = ")
frequency = float(input("Frequency = "))
correct_answers = int(input("Correct Answers = "))

grade = None
if frequency < 75:
    grade = "Fail"
elif correct_answers <= 10:
    grade = "D"
elif correct_answers <= 15:
    grade = "C"
elif correct_answers <= 20:
    grade = "B"
else:
    grade = "A"

print("Name = {0}; Grade = {1}".format(name, grade))
