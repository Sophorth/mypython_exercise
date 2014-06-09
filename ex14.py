from sys import argv
script, user_name = argv

print "\n ------Start Exercise 14, Prompting and Passing ------\n"

print "Hi %s, I am in %s" % (user_name, script)
print "I'd like to ask you some question"
prompt = '>>'

print "How old are you?"
age = raw_input(prompt)

print "How many bike do you have?"
bike = raw_input(prompt)

print "Thanks for your answer, so %s you are %s year-old and you have %s bikes" % (user_name,age,bike)

print "\n ----------End Exercise 14 ---------------\n"