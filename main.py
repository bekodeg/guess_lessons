from pprint import pprint


def parse(arr):
    res = []
    if arr[0][-1] == ':':
        r = parse(arr[1:])
        res.append((arr[0][:-1], r[0]))
        arr = r[1]
    else:
        res.append(arr[0][:-1])
        arr = arr[1:]
    if arr[0][-1] == ':':
        r = parse(arr[1:])
        res.append((arr[0][:-1], r[0]))
        arr = r[1]
    else:
        res.append(arr[0][:-1])
        arr = arr[1:]
    return res, arr


with open('questions.txt', 'rt', encoding='utf-8') as file:
    read = file.readlines()
    read = list(map(lambda s: s.strip(), read))
    data = (read[0], parse(read[1:])[0])
    while True:
        print(data[0])
        data = data[1]
        v = input().lower()
        if v == 'нет':
            data = data[1]
        else:
            data = data[0]
        if type(data) == str:
            print(data)
            break
