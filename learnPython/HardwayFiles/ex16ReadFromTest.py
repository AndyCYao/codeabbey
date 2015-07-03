from sys import argv
script, filename = argv
print("Andy - going to print out whatever is in the test.txt \n")
txt = open(filename)
print("Here's the file")

print(txt.read())
