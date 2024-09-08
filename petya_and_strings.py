f_line = input().lower()
s_line = input().lower()
r = 0

for i in range(len(f_line)):
    f = f_line[i]
    s = s_line[i]

    if f > s:
        r = 1
        break
    if f < s:
        r = -1
        break

print(r)