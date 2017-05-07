#! python3

# write will replace whatever was there while append will add it to the end

text = 'Sample text to save\nNew Line!'

# opens the file or creates one if not already there. We also have to pick if
# we want to read, append or write of which we chose write here.
# Side note, you always want to close
saveFile = open('exampleFile.txt', 'w')
saveFile.write(text)
saveFile.close()

