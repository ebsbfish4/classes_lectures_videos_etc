#! python3

# This variable has no function and is in the global scope, but it is
# not a global variable

x = 6

def example():
    z=5
    print(z,x)
    print(x+5)
    # This line causes an error  
    # x+=1
example()


# This works because x is set as a global variable
def example_1():
    global x
    print(x)
    x+=5
    print(x)

example_1()

# This is how you can kind of get around it if you do not want to use
# a global variable. You can also return globx to keep the value
def example_2():
    globx = x
    print(globx)
    globx += 5
    print(globx)

example_2()

