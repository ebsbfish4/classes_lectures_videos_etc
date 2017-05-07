#! python3

'''
Both lists and tuples are "lists" by the everyday definition, but the
main difference is that a tuple is immutable and a list is mutable. This just
means that you cannot change a tuple after it has been created, but you can
make changes to lists (add, remove, change values, sort, etc.
'''

x = 5,6,2,6 # This is a tuple
x = (5,6,2,6) # Another tuple

y = [5,6,2,6] # A list! Square brackets

'''
Realistically, you do not really need to use tuples often (except for
sequence unpacking?) unless you really have a list that you know us never
going to change. A tuple is created and iterated through faster than a list.
So for a large assortment of unchanging data makes sense.
'''

def exampleFunc():
    #Does a bunch of stuff
    return 15,6

x,y = exampleFunc()

# Indexes of lists and tuples both start at 0
