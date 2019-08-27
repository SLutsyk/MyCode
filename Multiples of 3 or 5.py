def solution(number):
    multiples = []
    for x in range(number):
        if x % 3 == 0 or x % 5 == 0:
            if x not in multiples:
                multiples.append(x)
    return sum(multiples)
