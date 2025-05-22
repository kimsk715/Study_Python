# import calc_add
# print(calc_add.add(2, 3))

# import calc_add as c
# print(c.add(2, 3))

# from calc_add import add
# print(add(2, 3))

# from calc_add import add, get_total
# from calc_add import *
# print(get_total(2, 3, 4))

# from calc_add import Calculator
#
# c = Calculator(3, 5)
# print(c.subtract())

import calc_add as c
calc = c.Calculator(3, 2)
print(calc.subtract())