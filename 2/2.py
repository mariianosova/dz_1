data = [line.rstrip() for line in open("input.txt")]
def get_sorting_data_from_line(line):
    line = line[2:]
    first = int(line.split(".")[0])
    second = int(line.split(".")[1].split("-")[0])
    third = line.split("-")[1].split(" ")[0]
    if "." in third:
        return [first, second] + list(map(int, third.split(".")))
    else:
        return [first, second, int(third)]
data.sort(key=get_sorting_data_from_line)
fout = open("output.txt", "w")
for line in data:
    print(line, file=fout)