from sys import argv
script, file_name = argv

print "\n ------Start Exercise 15, Reading file ------\n"

print "You are tryng to open a file named: ", file_name
print "and here is your file content: \n"

txt = open(file_name)
print txt.read()

print "\n End of your file \n"