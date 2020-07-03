from maths.basic_functions import add
from maths.extra_functions import tables

# call functions

print("add two numbers:")
print()
numberOne = int(input("enter firts number: "))
numberTwo = int(input("enter second number: "))
result = add(numberOne, numberTwo)
print()
print("the result is: {}".format(result))


print("call function table:")

tables(5)

