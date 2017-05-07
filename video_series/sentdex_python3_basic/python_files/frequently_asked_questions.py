#! python3

'''
What does the line do?

#!/usr/bin/python

If you are on linux, it gives the path to python. This doesn't really
have the same use on windows. Another thing you will see quite often in
modules is

def epic():
    print('wow this is great!')

if __name__ == '__main__':
    print('such great module!!!!')

Why do people write if name == main? So people can use this code as a
module. If in another script, you wanted to import that last module
(file titled epicthing), you would use

import epicthing

epicthing.epic()

The reason we used name == main is so that the print statement it would not
run it. If we did not have that line, when it was imported in our
other module the line such a great module would have run. Basically,
what that line is asking is if this module is the main file being run.
'''
