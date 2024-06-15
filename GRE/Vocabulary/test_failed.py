#!/usr/bin/python3
import sys

filename = "failed.md"

f = open(filename, "r")

if not f:
    print("File %s does not exist"%(filename))
    exit(1)
    
residual_lines = []

while True:
    line = f.readline()
    if not line:
        break
    tokens = line.split("|")
    if len(tokens) < 4:
        break
    word = tokens[2]
    trans = tokens[3]
    print(word)
    inputline = input()
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
