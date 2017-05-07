#! python3

'''
The idea of classes is to encase a group. Can be used like a module
A python module is nothing but a package to encapsulate reusable code.
They reside in a folder with a __init__.py file. Modules can
contain functions and also classes. Modules are imported using the
"import" keyword. Classes can either be defined in your main application
or inside modules imported by your application. Classes can contain
properties and methods.
'''

class calculator:

    def addition(x,y):
        added = x+y
        print(added)

    def subtraction(x,y):
        sub = x - y
        print(sub)

    def multiplication(x,y):
        mult = x * y
        print(mult)
        
    def division(x,y):
        div = x / y
        print(div)


calculator.multiplication(3,5)
