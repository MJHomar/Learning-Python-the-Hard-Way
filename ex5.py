# this variable "cars" stores the total amount of cars
cars = 100

# This variable "space_in_a_car" stores the Maximum seating allowed per car
space_in_a_car = 4.0

# This variable "drivers" stores the total amount of drivers
drivers = 30

# This variable "passengers" is the total number of passengers
passengers = 90

# This variable "cars_not_driven" is the amount of cars not going to be used because there are not enough drivers.
cars_not_driven = cars - drivers

# This variable "cars_driven" is the amount of cars in use based on total drivers available
cars_driven = drivers

# This variable "carpool_capacity" is based on the total amount of cars to be driven (drivers) time the maximum seating of each car
carpool_capacity = cars_driven * space_in_a_car

# This variable "average_passengers_per_car" is determined by the total passengers by the total cars driven
average_passengers_per_car = passengers / cars_driven

# These print statements will print out the various text strings with the numbers in them.
print "There are", cars, "cars avaiable."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "WE can transport", carpool_capacity, "people today."
print "We have", passengers, "passengers to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
