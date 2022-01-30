def is_parent(child, parent):
    if child == parent:
        return True
    for p in parents[child]:
        if is_parent(p, parent):
            return True
    return False


def bubbleSort(data):
    lenght = len(data)
    for iIndex in range(lenght):
        swapped = False
        for jIndex in range(0, lenght - iIndex - 1):
            if data[jIndex] > data[jIndex + 1]:
                data[jIndex], data[jIndex + 1] = data[jIndex + 1], data[jIndex]
                c[jIndex], c[jIndex + 1] = c[jIndex + 1], c[jIndex]
                swapped = True
        if swapped == False:
            break


n = int(input())

parents = {}
for _ in range(n):
    a = input().split()
    parents[a[0]] = [] if len(a) == 1 else a[2:]

q = int(input())
b = []
c = []
n = []
for _ in range(q):
    a = input()
    b.append(a)

for i in range(len(b)):
    for j in range(i + 1, len(b)):
        if is_parent(b[j], b[i]):
            if b[j] not in c:
                n.append(j)
                c.append(b[j])
bubbleSort(n)
for s in c:
    print(s)
