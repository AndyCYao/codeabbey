from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file))

# we could do these two on one line
in_file = open(from_file)
indata = in_file.read()

print("these files are %d bytes long" % len(indata))
print("does the output file exists? %r" % exists(to_file))
print("ready, hit return to continue, ctrl c to abort")
input("?")

out_file = open(to_file, 'w')
out_file.write(indata)

print("we're done")

# out_file.close()
# in_file.close()
