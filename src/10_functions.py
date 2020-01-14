# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
userInput = input("Enter a number: ")
# num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"


# YOUR CODE HERE
def is_even(hot_fiyah):
    # First lets do type checking for number, string, float
    try:
        val = int(hot_fiyah)
    except ValueError:
        try:
            val = float(hot_fiyah)
            return print("Itsa floaty! No a likey a stringys!", val)
        except ValueError:
            return print("Itsa stringy!")
    # Now, in order to get to this point we must have a number.
    # Let's check to see if it's divisible by 2. Trigger the
    # appropriate response.
    if val % 2 == 0:
        print("\nEven!\n")
    else:
        print("\nOdd!\n")


is_even(userInput)
