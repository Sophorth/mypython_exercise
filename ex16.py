from sys import argv

script, file_name = argv

print "\n ------Start Exercise 16, Read and Write to file ------\n"

print "We are going to clear the file and write some new content into it."
print "If you are not OK with this just press Ctrl + C"
print "Or if you are OK, just press return:"
raw_input("???")

print "\n OK now we are ready to clear the file:\n"

myfile = open(file_name, 'w')
myfile.truncate()

print "Let input some text into the file:"
new_text1 = raw_input(">")

print "Let add some more text:"
new_text2 = raw_input(">")

myfile.write(new_text1)
myfile.write("\n")
myfile.write(new_text2)

print "\n Thank You very much. The file has been saved with new content \n"

myfile.close()