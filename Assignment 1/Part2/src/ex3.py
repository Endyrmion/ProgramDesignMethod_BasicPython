# 3. Imagine that you teach three classes.
# These classes have 32, 45, and 51 students.
# You want to divide the students in these classes into groups with the same number of students in each group, but you recognize that there may be some “left over” students.
# Assume that you would like there to be 5 groups in the first class (of 32 students), 7 groups in the second class (of 45 students), and 6 groups in the third class (of 51 students).
# Write a program to calculate the number of students in each group (where each group has the same number of students).
# Print this number for each class and also print the number of students that will be “leftover” (i.e., the number of students short of a full group).
# Use simultaneous assignment to assign the number in each group and the “leftover” to variables. The following demonstrates the program’s output:
#
# Number of students in each group: Class 1: 6 Class 2: 6 Class 3: 8
# Number of students leftover:  Class 1: 2 Class 2: 3 Class 3: 3


try:
    student1 = int(input("Class 1) Student amount:\n-> "))
    nbGroup1 = int(input("Class 1) Group wanted :\n-> "))
    student2 = int(input("Class 2) Student amount:\n-> "))
    nbGroup2 = int(input("Class 2) Group wanted\n-> "))
    student3 = int(input("Class 3) Student amount:\n-> "))
    nbGroup3 = int(input("Class 3) Group wanted\n-> "))
except:
    print("Wrong input")
    exit()

# PART 1
groupSize1 = student1 / nbGroup1
leftOvers1 = student1 % nbGroup1
print("Class 1\n Students: %d\n Groups: %d\n Students Per Group: %d\nLeftover students: %d" % (student1, nbGroup1, groupSize1, leftOvers1))


# PART 2
groupSize2 = student2 / nbGroup2
leftOvers2 = student2 % nbGroup2
print("Class 2\n Students: %d\n Groups: %d\n Students Per Group: %d\nLeftover students: %d" % (student2, nbGroup2, groupSize2, leftOvers2))


# PART 3
groupSize3 = student3 / nbGroup3
leftOvers3 = student3 % nbGroup3
print("Class 3\n Students: %d\n Groups: %d\n Students Per Group: %d\nLeftover students: %d" % (student3, nbGroup3, groupSize3, leftOvers3))
