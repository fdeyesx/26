f = open('26 (3).txt')
n = int(f.readline())
a = [0] * 1500
for s in f:
    x, y = map(int, s.split())
    for i in range(x, y + 1):
        a[i] += 1

mx = max(a)
k = 0
for i in range(1, len(a)):
    if a[i] == mx and a[i - 1] < mx:
        k += 1
print(k, mx)

