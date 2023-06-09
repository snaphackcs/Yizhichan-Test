
#keyboard_str = input("")
#keyboard_str = "qwertyuiopasdfghjklzxcvbnm" #QWERTY
#keyboard_str = "pyfgcrlaoeuidhtnszqjkxbmwv" #DVORAK_modified
#keyboard_str = "qwfpgjluyarstdhneiozxcvbkm" #COLEMAK

alpha_place = [0] * 26
row1 = []
row2 = []
row3 = []
for i in range(len(keyboard_str)):
    if i <= 9:
        row1.append(keyboard_str[i])
        alpha_place[ord(keyboard_str[i]) - ord('a')] = [0, i]
    elif i <= 18:
        row2.append(keyboard_str[i])
        alpha_place[ord(keyboard_str[i]) - ord('a')] = [1, i - 10]
    else:
        row3.append(keyboard_str[i])
        alpha_place[ord(keyboard_str[i]) - ord('a')] = [2, i - 19]
keyboard_list = [row1, row2, row3]
#print(keyboard_list)
#print(alpha_place)

dist = []
for i in range(26):
    row = []
    i_row = alpha_place[i][0]
    for j in range(26):
        j_row = alpha_place[j][0]
        if i_row == j_row:
            row.append(abs(alpha_place[i][1] - alpha_place[j][1]) * 4)
            # print(abs(alpha_place[i][1] - alpha_place[j][1]) * 4, 0)
        else:
            if abs(i_row - j_row) == 2:
                phase_shift = 3
            elif i_row * j_row == 0:
                phase_shift = 1
            else:
                phase_shift = 2
            # print(phase_shift, abs(alpha_place[i][1] - alpha_place[j][1]) * 4 + phase_shift, (i_row - j_row) * 4)
            row.append(((abs(alpha_place[i][1] - alpha_place[j][1]) * 4 + phase_shift) ** 2 + ((i_row - j_row) * 4) ** 2) ** 0.5)
    dist.append(row)
#print(dist)

f = open('GRE_8000_Words.txt', encoding='utf-8')
data = f.readlines()

total = 0
for word in data:
    for i in range(len(word) - 2):
        if word[:-1].isalpha() and not 'é' in word:
            word = word.lower()
            # print(word, word[i], word[i+1])
            total += dist[ord(word[i]) - ord('a')][ord(word[i + 1]) - ord('a')]
print("Total distance typing:", total * 4.7625 / 1000000, "km")
