#! python3

# Eval evaluates the expression you give it in the form of a string
# and returns the value. Why might you want to do this?

list_str = "[5,6,2,1,2]"

# This list is a string

list_str = eval(list_str)

print(list_str)
print(list_str[2])

x = input("code:")
check_this_out = eval(input("code:"))

# exec can do everything eval can and a little more
