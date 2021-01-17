def count_num(num: int) -> int:
    count = 99

    if 1 <= num <= 99:
        return num

    for i in range(100, num + 1):
        a = i // 100
        b = (i - 100 * a) //10
        c = i % 10

        if a-b == b-c:
            count += 1
            
    return count

input_num = int(input())
print(count_num(input_num))
