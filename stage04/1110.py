input_str = input()
input_num = int(input_str)
new_num = int(input_str)
cycle = 0

while True:

    if new_num < 10:
        new_str = '0' + str(new_num)
    else:
        new_str = str(new_num)

    mid_num = int(new_str[0]) + int(new_str[1])

    if mid_num < 10:
        mid_str = '0' + str(mid_num)
    else:
        mid_str = str(mid_num)

    last_str = new_str[1] + mid_str[1]
    new_num = int(last_str)
    cycle += 1

    if new_num == input_num:
        break

print(cycle)
