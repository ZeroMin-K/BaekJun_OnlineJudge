case = int(input())

for _ in range(case):
    x, y = map(int, input().split())

    count = 0
    distance = y - x

    move = 1        # count 별 이동 가능 거리 
    move_plus = 0  # 이동 거리의 합

    while move_plus < distance:
        count += 1
        move_plus += move    #count 수에 해당하는 move 더함
        if count % 2 == 0:  # count가 2의 배수 일 때
            move += 1
    print(count)
