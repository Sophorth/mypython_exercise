# Hello this my revise
from sys import argv

script, name = argv 

print "\nThis is revise lesson \n"
print "\nHello ", name

print "Let me diagnos your illness"
print "\nPlease anwer the following question :"
print "\nWhat is your mood today?"
print "\na- Sad \nb- Happy"
answer = raw_input("Choose a or b: ")
if answer == 'a':
	print "\nYou are Depress. You should consult with Dr. Kalinna"
elif answer == 'b':
	print "\nYou are Menia. Please go see Mr. Sophorth's wife"
else:
    print "\nI have no idea because you didn't choose a or b"

print "\nBye for now! \n"