# 2. Write a program that calculates the average score on an exam. Assume we have a small class of only three students.
# Assign each student’s score to variables called student1, student2, and student3 and then use these variables to find the average score.
# Assign the average to a variable called average. Print the student scores and the average score.
# The following demonstrates the program output when the students have been assigned scores of 80.0, 90.0, and 66.5:
# Student scores:  80.0 90.0 66.5 Average: 78.83333333333333

def ex2_average_grade():
    try:
        student1 = int(input("STUDENT 1 ?\n-> "))
        student2 = int(input("STUDENT 2 ?\n-> "))
        student3 = int(input("STUDENT 3 ?\n-> "))
    except:
        print("Wrong input.")
        exit()
    sum = student1 + student2 + student3
    average = sum / 3
    print("Students grades are:\nStudent1: %f\nStudent2: %f\nStudent3: %f\nAverage: %f" % (student1, student2, student3, average))

ex2_average_grade()
