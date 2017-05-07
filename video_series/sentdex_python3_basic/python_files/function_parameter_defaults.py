#! python3

# This is how you normally define a function
def simple(num1,num2):
    pass

# This just gives a default value of 5. You can run this without
# a value for the second one because it has a default value.
def simple(num1, num2=5):
    print(num1, num2)

simple(2)

# You can use default parameters to have basics for something or
# give the user the chance to customize.
def basic_window(width,height,font='TNR',
                 bgc='w',scrollbar=True):
    print(width,height,font,bgc)


basic_window(500,350)
basic_window(500,350,bgc='b')
