# Write Python code to print out how far light travels
# in centimeters in one nanosecond.  Use the values
# defined below.
# speed_of_light = 299792458   meters per second
# centimeters = 100            one meter is 100 centimeters
# nanosecond = 1.0/1000000000  one billionth of a second

speed_of_light = 299792458   #meters per second
centimeters = 100            #one meter is 100 centimeters
nanosecond = 1.0/1000000000  #one billionth of a second

Answer =  (speed_of_light*centimeters*nanosecond)
print(Answer, "cm")