#! python3

# A module is just a python script (some are a little more)
# The standard python modules will be in lib, the third party
# modules will be installed in site-packages.

# You can change the name when you import to a shorter name

import statistics as s

print(s.mean([1,2,3]))

'''
If you want to just import variance and type it, you can do

from statistics import variance
print(variance([1,2,3]))

you can add an as to that as well

from statistics import variance as v

if you need to import a few things from statistics you can do

from statistics import variance, mean

use shorter names
from statistics import variance as v, mean as m

If you want to only use the specific names but want to import
everything from statistics, you can use

from statistics import *

and you can then use

variance([1,2,3])
mean([1,2,3])

'''




