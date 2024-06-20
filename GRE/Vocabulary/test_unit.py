#!/usr/bin/python3
import sys

n = len(sys.argv)
 
if n != 2:
    print("Pass which day you want to review as command line arg")
    exit(1)

filename = "Day%s.md"%(sys.argv[1])
wfilename = "failed.md"

f = open(filename, "r")
wf = open(wfilename, "a")

if not f:
    print("File %s does not exist"%(filename))
    exit(1)

f.readline()
f.readline()

peek = False

while True:
    if not peek:
        line = f.readline()
    else:
        peek = False
    if not line:
        break
    tokens = line.split("|")
    if len(tokens) < 4:
        break
    word = tokens[2]
    trans = tokens[3]
    print(word)
    inputline = input()
    if inputline == "p":
        peek = True
        print(trans)
    if inputline == "q":
        break
    if inputline == "x":
        print(trans)
        wf.write(line)
        
f.close()
wf.close()

exit(0)
