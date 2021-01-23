a, b, c = map(int, input().split())

if c - b <= 0:
    point = -1
else:
    point = int((a / (c-b)) + 1) 

print(point)
