#!/usr/bin/python3
import sys

filename = "failed.md"

f = open(filename, "r")

if not f:
    print("File %s does not exist"%(filename))
    exit(1)

start_pos = f.tell()
num_total_lines = len(f.readlines())
f.seek(start_pos)

residual_lines = []

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
    
    No = tokens[1]
    No = No.strip()
    word = tokens[2]
    trans = tokens[3]
    print("[%s/%d] %s"%(No, num_total_lines, word))
    inputline = input()
    if inputline == "p":
        peek = True
        print(trans)
    if inputline == "q":
        break
    if inputline == "x":
        print(trans)
        residual_lines.append(line)

residual_lines += f.readlines()

f.close()

f = open(filename, "w")

for line in residual_lines:
    f.write(line)
    
f.close()

exit(0)
