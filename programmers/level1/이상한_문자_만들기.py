def solution(s):
    split_s = s.split(" ")

    for n, word in enumerate(split_s):
        a = ""
        for i, ss in enumerate(word):
            if i % 2 == 0:
                a += ss.upper()

            else:
                a += ss.lower()
        split_s[n] = a

    return " ".join(split_s)