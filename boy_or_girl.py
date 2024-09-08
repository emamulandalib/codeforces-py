inp = input()
res = 0
distinct_letters = set()

for c in inp:
    distinct_letters.add(c)

if len(distinct_letters) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')