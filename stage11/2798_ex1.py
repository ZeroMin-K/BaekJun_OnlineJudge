n, m = map(int, input().split())
card_list = list(map(int, input().split()))
list_len = len(card_list)
sum = 0

for i in range(list_len -2):
    for j in range(i+1, list_len - 1):
        for k in range(j+1, list_len):
            if card_list[i] + card_list[j] + card_list[k] > m:
                continue
            else:
                sum = max(sum, card_list[i] + card_list[j] + card_list[k])

print(sum)
