#!/usr/bin/env python2
from hashlib import md5
import sys
import os

class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream
    def write(self, data):
        self.stream.write(data)
        self.stream.flush()
    def writelines(self, datas):
        self.stream.writelines(datas)
        self.stream.flush()
    def __getattr__(self, attr):
        return getattr(self.stream, attr)

sys.stdout = Unbuffered(sys.stdout)

def md5_hash(s):
    return md5(s).hexdigest()

def main():
    passcode = str(input("Enter passcode: "))
    if md5_hash(passcode) == "675ba33a8b6aeaf531f4e4bf9f162ab3":
        os.system("cat /var/flag/*")
    else:
        print "Invalid passcode"

if __name__ == '__main__':
    main()