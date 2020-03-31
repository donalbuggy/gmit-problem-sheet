# Donal Buggy
# file to take the name/location of a text file as an argument on the command line, read its contents into a string variable, then count the number of times the letter 'e' is used in the string

import sys

f = open(sys.argv[1], 'r') # opens file via command line argument to a variable 'f'

text = f.read()

print(text.count('e')) # uses the count() method to count the instances of the argument character

f.close()

# consulted stackoverflow.com (https://stackoverflow.com/questions/7439145/i-want-to-read-in-a-file-from-the-command-line-in-python/7439162) to use take filename as command line argument

# consulted tutorialspoint.com (https://www.tutorialspoint.com/python/list_count.htm) to use count() method