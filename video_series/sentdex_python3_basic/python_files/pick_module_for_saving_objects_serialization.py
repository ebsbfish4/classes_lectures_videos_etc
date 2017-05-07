#! python3

# This converts python to bytestream and back again.
# In python this is refered to as pickling. This is
# used to store an object (which can be just about anything)
# One example is if you train a classifier in a machine learning
# algorithm you can pickle the object in oreder to onot have to
# retrain it every time you need it.
# It can also be useful if you are interacting with a largre
# dataset. Basically it can make these loading proccesses faster,
# sometimes up to 100x or 1000x. AKA useful for anything that requires
# a lot of processing and ends in an object.

# You might use pickles to do something like transfer data
# between servers, from another source, etc. Pickle has no
# security in place, so you could run some nefarious code.

import pickle

example_dict = {1:"6",2:"2",3:"f"}

# This is how you create a pickle
#pickle_out = open("dict.pickle","wb")
#pickle.dump(example_dict, pickle_out)
#pickle_out.close()


pickle_in = open("dict.pickle","rb")
example_dict = pickle.load(pickle_in)

print(example_dict)
print(example_dict[2])


