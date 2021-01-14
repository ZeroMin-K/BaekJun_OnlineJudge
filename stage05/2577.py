a = int(input())
b = int(input())
c = int(input())

array = str(a * b * c)
dict = {}

for i in range(0, 9+1):
    dict[i] = 0

for key in array:
    dict[int(key)] += 1

for i in dict:
    print(dict[i])
