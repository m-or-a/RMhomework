arr = [int(i) for i in input('arr = ').split()]
k = int(input('k = '))

d = {}
for i in range(len(arr)):
    if arr[i] in d:
        d[arr[i]] += 1
    else:
        d[arr[i]] = 1

sort_d = sorted(d, key = d.get, reverse = True)

print(sort_d[0:k])

