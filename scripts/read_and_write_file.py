#!/usr/bin/env python

# This script is to show an example of reading and writing a file

# first we need to open the file in order to be able to read it
# it is like loading it to python environment
file = open("../files/simple_string.txt")

# read the file
string = file.read()

# print it
print(string)

# substitute //n to /n since we want it to be a new line
new_lines_string = string.replace('\\n', '\n')

# print it to see how it looks
print(new_lines_string)

# write that to a txt file

# first we will open a txt file in the writing mode (therefore the "w")
with open("../files/poem.txt", "w") as f:
# and then actually write it with print, so the new lines can be preserved
    print(new_lines_string, file = f)

# important: you need to specify the parameter 'file=' for 'f', otherwise it won't work





