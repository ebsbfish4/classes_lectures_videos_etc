#! python3

# Idea of urllib is to allow you to access the internet with
# python.

# In python 2.7 you just had to import urllib, but now
# you have to specify
import urllib.request
import urllib.parse

# This will print the source code of google.com
#x = urllib.request.urlopen('https://www.google.com')
#print(x.read())

# Generally when you access a url you will most likely only care
# about something specific, like paragraph text for example. To
# parse this requires importing a different module.
'''
url = 'https://pythonprogramming.net'
values = {'s':'basic','submit':'Search'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()

print(respData)
'''
# Sometimes when you visit a website with a programming language
# like python, the owners of the website do not want you doing that
# so if they detect it they may block you.

# This, for eaxample, will fail with an HTTP 403 error because
# google recognizes that it is a program
try:
    x = urllib.request.urlopen('https://www.google.com/search?q=test')
    print(x.read())

except Exception as e:
    print(str(e))

try:
    url = 'https://www.google.com/search?q=test'
    headers = {}
    headers['User-Agent'] = ''
except Exception as e:
    print(str(e))

