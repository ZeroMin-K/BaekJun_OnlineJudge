count = 0
line = int(input())

for i in range(line):
    string = input()
    word_occur = list()

    is_group = True
    before = string[0]
    for i in range(len(string)):
        if string[i] not in word_occur:
            word_occur.append(string[i])
        else:
            if string[i] != before:
                is_group = False
                break
        before = string[i]
    
    if is_group:
        count += 1

print(count)
