words = open("input.txt").readline().rstrip().split()
i = 0
fout = open("output.txt", "w")
while i < len(words):
    line = ""
    while True:
        word = words[i]
        if (line == "" and len(word) <= 20):
            line += word
            i += 1
            if i == len(words):
                break
        elif line != "" and len(line + " " + word) <= 20:
            line += " " + word
            i += 1
            if i == len(words):
                break
        else:
            break
    print(line, file=fout)

