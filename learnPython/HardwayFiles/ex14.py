from sys import argv

script, user_name = argv
prompt = 'your answer '

print ("Hi %s, I am the %s script." %(user_name,
       script))

print("Do you like me %s?" %(user_name))
likes = raw_input(prompt)

print("Where do you live %s" %(user_name))
lives = raw_input(prompt)

print("What kind of computer do you have")
computer = raw_input(prompt)

print("""
Alright, you have said %r about liking me.
You live in %r. not sure about where that is.
and you have a %r computer. nice.
""" %(likes, lives, computer))
