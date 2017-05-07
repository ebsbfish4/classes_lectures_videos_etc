#! python3

'''
A module is usually just a python script

def ex(data):
    print(data)

Save that file as examplemod.py
Now in original script

import examplemod

This will have an error because the path it will go through to
look for modules is local, site-packages and lib. Typically third
party modules will be in site packages while standard ones will
be in lib.

If you move the module to site-packages, then

import examplemod
examplemod.ex(5)

should work
