"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated.

Take a look at
https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

""" Example from docs
squares = []
    for x in range(10):
        squares.append(x**2)

>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]
y = [number for number in range(1, 6)]
print(y)

# for x in range(5):
#     y.append(x + 1)
# y = []
# for x in range(1, 6):
#     y.append(x)
# print(y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
y = [x**3 for x in range(10)]
print(y)

# for x in range(10):
#     y.append(x ** 3)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".
a = ["foo", "bar", "baz"]

y = [x.upper() for x in a]
print(y)
# for x in a:
#     y.append(x.upper())


# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.
x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
y = [incoming_input for incoming_input in x if int(incoming_input) % 2 == 0]
# Changing type to int is not necessary
# y = [int(incoming_input) for incoming_input in x if int(incoming_input) % 2 == 0]

print(y)

# for input in x:
#     input_num = int(input)
#     if input_num % 2 == 0:
#         y.append(input_num)
