#!/usr/bin/python3
import sys
import os

n = len(sys.argv)
 
if n != 2:
    print("Pass which day you want to review as command line arg")
    exit(1)

filename = "Day%s.md"%(sys.argv[1])
wfilename = "temp.md"

f = open(filename, "r")
wf = open(wfilename, "w")

if not f:
    print("File %s does not exist"%(filename))
    exit(1)

lineCount = 1

while True:
    line = f.readline()
    if not line:
        break
    if len(line) < 2:
        continue
    tokens = line.split("|")
    if len(tokens) < 4:
        break
    oldNo = tokens[1]
    oldNo = oldNo.strip()
    try:
        if len(oldNo) != 0:
            oldNo = int(oldNo)
    except:
        wf.write(line)
        continue
    
    no = str(lineCount)
    word = tokens[2]
    trans = tokens[3]
    wf.write("| %d | %s | %s |\n"%(lineCount, word, trans))
    lineCount += 1
    
f.close()
wf.close()

os.rename(wfilename, filename)

print("%s has been numbered"%(filename))

exit(0)
