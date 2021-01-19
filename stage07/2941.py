cro_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

string = input()

for word in cro_alpha:
    # 입력받은 문자열에서 크로아티아 알파벳 리스트에 해당하는 것을 바꿔줌
    string = string.replace(word, '*')

print(len(string))