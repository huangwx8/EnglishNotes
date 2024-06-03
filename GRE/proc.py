f = open("Vocabulary_Day1_processed.md", "w")

nline = 0

with open("Vocabulary_Day1.md", 'r') as i_file:
    while True:
        line = i_file.readline()
        if not line:
            break
        nline += 1
        line = line.replace("- ", "%d. "%(nline))
        f.write(line)