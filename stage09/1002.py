import math

case = int(input())

for _ in range(case):
    x1, y1, r1, x2, y2, r2 = map(int, input().split()) 

    count = 0

    dist = math.sqrt((x2 - x1)**2+ (y2 - y1)**2)

    max_r = max(r1, r2)
    min_r = min(r1, r2)

    if dist == 0 and r1 == r2:
        count = -1
    elif dist == r1 + r2 or max_r == min_r + dist:
        count = 1
    elif dist > r1 + r2 or max_r > min_r + dist:
        count = 0
    else:
        count = 2

    print(count)
