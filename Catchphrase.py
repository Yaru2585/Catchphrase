import glob
import os
import sys
import re

savedlines = []


def startreading():
    if os.path.isdir(sys.argv[1]):
        os.chdir(sys.argv[1])
        target = sys.argv[2]  # TODO: Multiple lines.
        for file in glob.glob("*.srt"):
            read(sys.argv[1], file, target)
        savelines()
        print("Finished!")

    else:
        print("Not a valid path!")


def savelines():
    try:
        outfile = open('result.txt', 'w')
        outfile.writelines(savedlines)
        outfile.close()
    except Exception as e:
        print("Something went wrong when saving the file: " + str(e))  # TODO: Custom exception.


def read(path, file, target):
    openfile = open(file, 'r')
    lines = openfile.readlines()
    for line in lines:
        if re.search(target, line, re.IGNORECASE):
            ln = line.strip()
            savedlines.append(ln + "\n")
            print(ln)
    openfile.close()


startreading()
