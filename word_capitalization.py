def word_capitalization():
    inp = input()
    f_letter_ord = ord(inp[0])

    if 65 <= f_letter_ord <= 90:
        print(inp)
        return

    inp = list(inp)
    cap_letter = f_letter_ord - 32
    inp[0] = chr(cap_letter)
    print("".join(inp))

word_capitalization()