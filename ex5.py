# Here we are collecting data points

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_in_centimeters = (height * 2.45)
weight = 180 # lbs
weight_in_kilograms = weight / 2.2
eyes = 'Blue'
teeth = 'White'
hair = "Brown"

# We are printing to the screen text strings and data from above
print "Let's talk about %s." % name
print "He's %d inches" % height, "or %d centimerters tall." % height_in_centimeters
print "He's %d pounds" % weight, "or %d kilograms heavy." % weight_in_kilograms
print "Actually that's not too heavy."
print "He has %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee he drinks! :-)" % teeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
