print " "
print " ------Start Exercise 11, Asking Question ------"
print " "
print "What is your name: ",
name = raw_input()
print "How tall are you: ",
height = raw_input()
print "How old are you: ",
age = raw_input()

print "You name is %s and your are %s inches tall and you are %s" % (name, height, age)

# We can do it in another way as bellow:

name = raw_input("What is your name? :")
height = raw_input("How tall are you? :")
age = raw_input("How old are you? :")

print "Again, Your name is %s and your are %s inches tall and you are %s" % (name, height, age)
