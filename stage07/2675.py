line = int(input())

for _ in range(line):
    count, string = input().split()
    count = int(count)
    for alpha in string:
        print(alpha * count, end = '')

    print()