def v1():
    one_x = 0
    one_y = 0
    for i in range(5):
        text = input()

        if "1" in text:
            nums = text.split(" ")
            for j in range(len(nums)):
                if nums[j] == "1":
                    one_x = j
                    one_y = i
                    break
            break
    f = abs(2 - one_x)
    s = abs(2 - one_y)
    print(f + s)


def v2():
    y = [2, 1, 0, 1, 2]
    for i in y:
        txt = input()
        if '1' in txt:
            print(i + y[txt.find("1") // 2])
            break