dict = {}
string = input().upper()
max_count = 0

for alpha in string:
    if alpha in dict:
        dict[alpha] += 1
    else:
        dict[alpha] = 1

count_list = dict.values()
max = max(count_list)

for num in count_list:
    if max == num:
        max_count += 1
        if max_count > 1:
            print('?')             
            exit()

for key in dict:
    if dict[key] == max:
        print(key)
        break
