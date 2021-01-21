count = 0
line = int(input())

for i in range(line):
    string = input()
    word_occur = list()

    is_group = True
    continued = False
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            if not continued:
                word_occur.append(string[i])
                continued = True
            continue
        else:
            if string[i] in word_occur:
                is_group = False
            else:
                word_occur.append(string[i])
    
    if is_group:
        count+= 1

    print(string, is_group, count)

print(count)
