n, x = map(int, input().split()) 

array = list(input().split())

for item in array:
    num = int(item)
    if num < x:
        print(num, end = ' ')


# 추가 답안 
""" n, x = map(int, input().split())
array = list(map(int, input().split()))

for i in range(n):
    if array[i] < x:
        print(array[i], end= ' ') """