#! python3

import sys

# This will print out test in the red error font. It is also
# good practice to "flush" the stderr after. stdout will print
# the blue text.

sys.stderr.write('test\n')
sys.stderr.flush()
sys.stdout.write('This is stdout text\n')


#


# This is the path to the file right now.

print(sys.argv)

# We can pass arguments into this file using our command line, which
# means you can use any other language(?)

if len(sys.argv) > 1:
    print(sys.argv[1])
    print(float(sys.argv[1]) + 5)
# You can pass arguments through the terminal, other languages, hackerish
