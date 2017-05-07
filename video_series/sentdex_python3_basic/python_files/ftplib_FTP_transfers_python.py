#! python3

# ftp stands for file transfer protocol. It is used to transfer
# files to remote servers. Today, apparently, ftp is not as useful
# and if you have anything even remotely secure you should use
# ssh because it is more secure.

from ftplib import FTP

ftp = FTP('domainname.com')

ftp.login(user='username', passwd='password')
ftp.cwd('/specificdomain-or-location/')

def grabFile():
    filename = 'filenName.txt'
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR'+ filename, localfile.write, 1024)
    ftp.quit()
    localfile.close()

def placeFile():
    filename = 'fileName.txt'
    ftp.storbinary('STOR '+file, open(filename, 'rb'))
    ftp.quit()
    
