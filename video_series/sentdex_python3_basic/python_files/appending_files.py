#! python3

# This will add to the end of the file, not erase what was there previously
appendMe = '\nNew bit of information'
appendFile = open('exampleFile.txt','a')
appendFile.write(appendMe)
appendFile.close()
