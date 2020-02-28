import glob
import os
import sys
import re


def startreading():
    if os.path.isdir(sys.argv[1]):
        os.chdir(sys.argv[1])
        target = sys.argv[2] #TODO: Multiple lines.
        for file in glob.glob("*.srt"):
            read(sys.argv[1], file, target)
    else:
        print("Not a valid path!")


def saveline(line):
    print("Not implemented yet")
    return


def read(path, file, target):
    print(path, file)
    openfile = open(file, 'r')
    lines = openfile.readlines()
    for line in lines:
        if re.search(target,line,re.IGNORECASE):
            saveline(line)
        print(line.strip())
    openfile.close()


startreading()
