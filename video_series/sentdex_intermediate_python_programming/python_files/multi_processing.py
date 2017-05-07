#! usr/bin/python3

# You might have noticed that when you run a python program, even if you
# use something like threading, your CPU does not get fully utilized. Why
# is this the case? It is that way because of the GIL (global interpreter lock),
# which was originally put in place as a memory management safeguard. It may not
# have been the best idea, and we have better ideas now, but the problem is you
# cannot now take out the GIL because a lot of infastructure is built with the
# assumption of that memory management safeguard being there.

# What multiprocessing does is allows you to utilize multiple processes (lol).
# E.g. you run one python script that maxes out at 16%, you open another that
# maxes out at 16%, etc. These are all called processes. What the multprocessing
# library allows you to do is launch seperate python processes that do not
# neccessarily talk to each other (they can).

import multiprocessing

def spawn(num,num1):
    print('Spawned {} {}!'.format(num,num1))


if __name__ == '__main__':
    for i in range(75):
        p = multiprocessing.Process(target=spawn, args=(i,i+1))
        p.start()
        #p.join()

# p.join() explained: If you ran this with p.join(), then you would see Spawned 0
# first followed by the rest in order. Without it, they will print whenver they are
# finished so they could get (very) out of order. If you are doing something to a database,
# or something like that, you most likely want to wait for the join()

# In next we will talk about sharing information between processes and how to get the
# return information of a function in multithreading (not just run the process like
# we did here.)
