from sys import argv
import time

script, filename = argv

print "Do you really want to erase %r?" % filename
print "To abort press Control + C" 
print "To accept press RETURN"

raw_input("?")

print "Opening file ..."

# without the 'w', I got "IOError: File not open for writing" when I tried to truncate.
target = open(filename)
#target = open(filename, 'w')

time.sleep(1)

print "Erasing contents..." 

target.truncate()

time.sleep(1)

target.write(raw_input("Type out something to replace the erased contents.\n > "))

print "Writing contents to the file"
time.sleep(1)
print "Closing the file..."

target.close()
time.sleep(1)
print "Ok, lets make sure those changes were saved properly"

target = open(filename)

time.sleep(1)
print target.read()