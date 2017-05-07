#!

from multiprocessing import Pool

def job(num):
    return num*2

print(job(3))

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(job, range(5)))


# I could not get this to run in IDLE, apparently it does not work but it works from
# the terminal. This comment is from the beginning of the documentation.
'''
Note Functionality within this package requires that the main module be importable by the children.
This is covered in Programming guidelines however it is worth pointing out here. This means that some
examples, such as the multiprocessing.Pool examples will not work in the interactive interpreter.
'''
