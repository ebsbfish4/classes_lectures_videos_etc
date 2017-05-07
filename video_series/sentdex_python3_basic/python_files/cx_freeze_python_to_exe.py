#! python3

# This is a third party module whose purpose is to convert python
# programming files into executables to better distribute to others.

# Distributing in compiled form makes it a little bit harder to steal
# your work.

# You set up one file with the code you want to distribute and
# you use a seperate file to tell the module how to set it up.
# This will be that setup file for an imaginary file

from ck_Freeze import setup, Executable

setup(name='urlParse',
      version = '0.1',
      description = 'Parse stuff',
      executables = [Executable('distme.py')

                     


# Then you go to the terminal and run python setup.py build from th
# directory that has the files inside of it.
