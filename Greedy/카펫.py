def solution(brown, yellow):
    x,y= 3,3

    while (1):
        guess_br = x * y - (x-2) * (y-2)
        guess_yellow = (x-2) * (y-2)

        if guess_yellow < yellow:
            y += 1
        elif guess_br > brown:
            x += 1
            y = x
        elif guess_br == brown and guess_yellow == yellow:
            return [max(x,y),min(x,y)]

print(solution(24,24))