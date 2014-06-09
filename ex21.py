# Exercise 21: Function can return something
print ' '

print "Now let try to return something for function\n"

def add(a, b):
	print ("Adding %d + %d") % (a, b)
	return a + b

def substract(a, b):
	print ("Substracting %d - %d") % (a, b)
	return a - b

def multiply(a, b):
	print ("Multiplying %d * %d") % (a, b)
	return a * b

def divide(a, b):
	print ("Dividing %d / %d") %  (a, b)
	return a / b

# OK now start calling function 

age = add(10, 5)
height = substract(100, 20)
weight = multiply(31, 4)
iq = divide(70, 2)

print ("\nAge: %d, Height: %d, Weight: %d, IQ: %d\n") % (age, height, weight, iq)

what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print "This is what look like: ", what, " Can you do it by hand\n"

