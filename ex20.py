# Exercise 20: Function and Files

from sys import argv

script, f_name = argv

print " "
print "We are going to use function to open a file\n"

def print_all(file_name):
	print file_name.read()

def rewind(file_name):
	file_name.seek(0)

def print_a_line(current_line, file_name):
	print current_line, file_name.readline() # print a line

current_file = open(f_name) # Open a file

print_all(current_file)
print " "

# Now let rewind to the beginning of the file

rewind(current_file)

line = 1

print_a_line(line, current_file)

line = line + 1
print_a_line(line, current_file)

line += 1
print_a_line(line, current_file)
