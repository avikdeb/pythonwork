from sys import argv
script,user_name = argv
prompt = ">"

print "Hi %s, I am  the %s script!" %(user_name,script)
print " I am going to ask you a few questions "

print "Do you like me?" , user_name
likes = raw_input( prompt )

print "Where do you live?" , user_name
lives = raw_input( prompt )

print """
Alright
You said %r about liking me 
and you said you live in %r
Dont know where that is ! 
"""  %( likes, lives )
