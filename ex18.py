# Exercise 18 - Name, Variable, Code Function
# This one is like your script

print " "
def print_two(*args):

	arg1, arg2 = args
	print ("arg1: %r and arg2: %r") % (arg1, arg2)

# OK that *args is pointless, we can just do This

def print_two_again(arg1, arg2):
	print ("arg1: %r and arg2: %r") % (arg1, arg2)

def print_one(arg):
	print "This one is", arg

def print_none():
	print "This is no argument."

print_two('Kalinna', 'Sophorth')
print_two_again('Sophorth','Kalinna')
print_one('Just One')
print_none()

print "\nAnother example of pass arguments:\n"

def cat_and_dog(num_cat, num_dog):
	print "There are %d cats and %d dogs" % (num_cat, num_dog)
	print "In total, I've got %s\n" % str(int(num_cat) + int(num_dog))

# Start calling the function with direct value
cat_and_dog(10, 30)

# Or we can call with varialble asinged
cat = 32
dog = 26
cat_and_dog(cat, dog)

# Or we can do the math in fuction call
cat_and_dog(2+3, 10-2)

# Or we can do the math and varibles
cat_and_dog(cat + 5, dog + 2)
cat_and_dog(cat + dog, cat * dog)
