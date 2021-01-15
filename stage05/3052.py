rest_dict = {}

for _ in range(10):
    rest = int(input()) % 42

    if rest not in rest_dict:
        rest_dict[rest] = 1
    else:
        rest_dict[rest] += 1

rest_list = rest_dict.keys()
print(len(rest_list))
