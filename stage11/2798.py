n, m = map(int, input().split())
card_list = list(map(int, input().split()))
card_list.sort()

prev_sum = 0
for i in range(len(card_list)):
    for j in range(i+1, len(card_list)):
        for k in range(j+1, len(card_list)):
            sum = card_list[i] + card_list[j] + card_list[k]
            if prev_sum < sum and sum <= m:
                prev_sum = sum 

print(prev_sum)
