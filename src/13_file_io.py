"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

f = open('workfile', 'w')
# If you don't use with, use close in conjuction with open
# like so:
f.close()

# With with
with open('workfile') as f:
    read_data = f.read()
# then close is optional. we can check with
f.closed

# mode is optional. r if omitted
# a appending
# w write
# r read
# r+ or w+ reading and writing
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# YOUR CODE HERE
with open("foo.txt") as foo_txt:
    read_data = foo_txt.read()

print('read_data:\n', read_data)


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain
# YOUR CODE HERE
with open("bar.txt", "w+") as bar_txt_create:
    bar_txt_create.write("hello, friend\nhow have you been?\nRead write and more!")

with open("bar.txt", "r") as bar_txt:
    read_data = bar_txt.read()

print('bar_txt: \n', read_data)
