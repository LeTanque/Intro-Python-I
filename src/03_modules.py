"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""
import sys
import os
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
# python 03_modules.py okay one two three
for argys in sys.argv:
    print(argys)


# Print out the OS platform you're using:
# YOUR CODE HERE
operating_sys = sys.platform
print("\nPlatform >>> ", operating_sys)

# Print out the version of Python you're using:
# YOUR CODE HERE
print("\nVersion Info >>> ", sys.version_info[0], ".", sys.version_info[1], ".", sys.version_info[2])
# or just
print("\nVersion Info >>> ", sys.version_info)
# Specifically stuff in the tuple
print("\nVersion Info >>> ", sys.version_info.releaselevel)


# Print the current process ID  using OS module
# YOUR CODE HERE
print("\nCurrent process ID >>> ", os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE
print("\nCurrent working directory >>> ", os.getcwd())


# Print out your machine's login name
# YOUR CODE HERE
print("\nMachine login name >>> ", os.environ["LOGNAME"])
