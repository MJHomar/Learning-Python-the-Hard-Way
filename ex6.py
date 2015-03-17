# This script is to practice the use of strings, variables, formats and to print them

# We are placing the number 10 for the variable %d
x = "There are %d types of people."  % 10

# We are placing the word binary for the variable binary
binary = "binary"

# We are placing the word don't for the variable do_not
do_not = "don't"

# Here we are placing the sting of words, "Those who know %s and those who %s." for the variable y,
# all the while placing the variable binary for the variable %s and the variable do_not for the variable %s
y = "Those who know %s and those who %s." % (binary, do_not)

# Printing to screen the 2 variables x and y
print x
print y

# Printing to screen the 2 stings of words with their variables x and y
print "I said: %r." % x
print "I also said: '%s'." % y

# We are placing the word False for the variable hilarious
hilarious = False

# We are placing the string of words, "Isn't that joke so funny?! %r" for the variable 
# Joke_evaluation, with a variable place holder to be inserted in the following print statement
joke_evaluation = "Isn't that joke so funny?! %r"

# We ar printing to the screen the string of words from the variable joke_evaluation and adding
# the word hilarious for the variable %r from the variable above
print joke_evaluation % hilarious

# We are placing the string of words, "This is the left side of..." for the variable  w
w = "This is the left side of..."
# We are placing the string of words, "a string with a right side." for the variable  e
e = "a string with a right side."

# Printing to screen the 2 variables w followed by e on the same line
print w + e
