test = int(input())

for i in range(test):
    h, w, n = map(int, input().split())

    floor = n % h 
    loc = n // h + 1

    if n % h == 0:
        floor = h
        loc = n // h 

    if loc < 10:
        loc = '0' + str(loc)

    room_num = str(floor) + str(loc)

    print(room_num)
