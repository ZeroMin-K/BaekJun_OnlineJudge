count = int(input())
sum = []
for i in range(0, count):
    x, y = map(int, input().split())
    sum.append(x+y)

for i in sum:
    print(i)