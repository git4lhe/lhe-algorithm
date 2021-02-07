from itertools import combinations


def solution(phone_book):
    for phone1, phone2 in combinations(phone_book, 2):
        n = min(len(phone1), len(phone2))
        if phone1[:n] == phone2[:n]:
            return False

    return True

print(solution(["12","123","1235","567","88"]))

phoneBook = ["12","123","1235","567","88"]
phoneBook = sorted()
for p1, p2 in zip(phoneBook, phoneBook[1:]):
    print(p1, p2)


print("12".startswith("1"))


def solution(citations):
    citations = sorted(citations, reverse=True)
    answer = 0

    for cite in citations:
        if cite > answer:
            answer += 1
        else:
            break
    return answer