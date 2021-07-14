x, y, w, h = map(int, input().split())

len_list = []

left = x
len_list.append(left)

right = w - x
len_list.append(right)

up = h - y
len_list.append(up)

down = y
len_list.append(down)

print(min(len_list))
