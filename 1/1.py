data = [line.rstrip().split(".")[1][1:] for line in open("input.txt")]
data.sort()
fout = open("output.csv", "w")
print("name,grade", file=fout)
for line in data:
    print(line[:-3] + "," + line[-1], file=fout)