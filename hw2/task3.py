from math import inf

def create_dict(times): 
    d = {}
    for i in range(len(times)):
        if times[i][0] not in d:
            d[times[i][0]] = {}
        d[times[i][0]][times[i][1]] = times[i][2]
    return d

def next_v(d, v, seen):
    sort_d = sorted(d[v], key = d[v].get, reverse = True)
    for i in sort_d:
        if i in d and i not in seen:
            return i
    return -1

def dkstra(times, n, x):
    weight = [inf for i in range(n)]   
    d = create_dict(times)              

    weight[x-1] = 0
    v = x
    seen = {v}

    if v not in d:
        return -1

    while v != -1:
        for key, value in d[v].items():
            if key not in seen:
                new_w = weight[v - 1] + value
                if new_w < weight[key - 1]:
                    weight[key - 1] = new_w
        v = next_v(d, v, seen)
        if v > 0:
            seen.add(v)

    if inf in weight:
        return -1

    return max(weight)

times = [list(map(int, i.split())) for i in input('times = ').split(',')]
n = int(input('N = '))
x = int(input('X = '))

t = dkstra(times, n, x)

print(t)
