from sys import argv
script, filename = argv

print("We're going to erase %r" % filename)
print("If you don't want that hit CTRL-C")
print("If you do, hit Return")

input("?")

print("Opening the file..")
target = open(filename, 'a')
# print("Truncating the file")
# target.truncate()

print("now im going to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("i'm going to write these to the file")

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print("Andy finally, we close it")
target.close()
