# 4. The Python statements below have several errors.
# Identify the errors and correct them so that the program properly calculates the circumference of Jimmy’s pie (circumference = 2*pi*r).
#
# pi = ’3.14’
# pie.diameter = 55.4
# pie_radius = pie.diameter // 2
# circumference = 2 * pi **
# pie_radius circumference-msg = ’Jimmy’s pie has a circumference: ’
# print(circumference-msg, circumference)
#
# The following demonstrates the output from the corrected program: Jimmy’s pie has a circumference: 173.956


def ex4():
    pi = 3.14
    pie_diameter = 55.4
    pie_radius = pie_diameter / 2    # ERROR THE / OPERATOR must be used ONCE
    circumference = 2 * pi * pie_radius # ERROR THE * OPERATOR must be used ONCE

    circumference_msg = "Jimmy’s pie has a circumference:" # ERROR, we must use the " instead of the '
    print(circumference_msg, circumference)

ex4()
