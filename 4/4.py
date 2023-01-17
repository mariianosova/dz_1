data = {}
for line in open("input.txt"):
    line = line.rstrip().split()
    for word in line:
        if word[-1] in [".", ",", ":"]:
            word = word[:-1]
        word = word.lower()
        if word not in data:
            data[word] = 0
        data[word] += 1
fout = open("output.txt", "w")
for elem in sorted(list(data.items()), key=lambda x: x[1], reverse=True)[:10]:
    print(elem[0] + "," + str(elem[1]), file=fout)