arr = [int(i) for i in input('arr = ').split()]
a = int(input('a = '))
b = int(input('a = '))
c = int(input('a = '))

triplets = 0
#explanation = []

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        for k in range(j+1, len(arr)):
            if (abs(arr[i] - arr[j]) <= a and 
                abs(arr[j] - arr[k]) <= b and
                abs(arr[i] - arr[k]) <= c):
                triplets += 1
#                explanation.append((arr[i], arr[j], arr[k]))

print(triplets)

#print('Triplets: ', explanation)

