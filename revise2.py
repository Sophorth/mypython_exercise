#------ This is revision 2 ------09 June 2014-----
# This exercise demonstrate Ex1 till Ex 17

from sys import argv
script, name = argv

print "Hello ", name, " How are you?"
ans = raw_input(">")

print "\nSo you just answer %r\n" % ans

a = 10
b = 25

print "10 + 25 =", a + b
print "\n10 * 25 =", a * b
print "\na > b is ", a > b
print "\na < b is ", a < b

print "\nNow we are going to open a file:"
print "What is your file name?"
file_name = raw_input(">")
txt = open(file_name)
print txt
print "\n", txt.read()

print "\nOK, %s now thanks for your time.\n" % name