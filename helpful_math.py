def helpful_math():
    inp = input()

    if len(inp) == 1:
        print(inp)
        return

    inp = inp.split("+")
    inp.sort()
    inp = "+".join(inp)
    print(inp)

helpful_math()