cell = [0]*210
f = open('26 (1).txt')
bags = []
for i in f:
    begin, end = i.split()
    begin, end = int(begin), int(end)
    bags.append([begin,end])

bags.sort()

k=0
for min in range(0,1440+1):
    for j in bags:
        if j[0] == min:
            if 0 in cell:
                first_0 = cell.index(0)
                last = first_0 + 1
                cell[first_0] = j[1]
                k += 1
    for j in range(210):
        if cell[j] == min:
            cell[j] = 0

print(k)
print(last)

"""210 1000
"""
