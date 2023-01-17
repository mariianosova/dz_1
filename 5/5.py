def main(strs):
    data = {}
    res = []
    strs_ord = list(map(lambda x: tuple(sorted(x)), strs))
    for i in range(len(strs)):
        ord = strs_ord[i]
        if ord not in data:
            data[ord] = []
        data[ord].append(strs[i])
    for elem in sorted(list(data.values()), key=lambda x: len(x)):
        res.append(sorted(elem))
    return res

print(main(["eat","tea","tan","ate","nat","bat"]))