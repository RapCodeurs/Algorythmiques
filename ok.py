a = [3, 8, 2, 4, 7]

def get_missing_numbers(l, min, max):
    b = []
    for i in range(min, max+1):
        if i not in l:
            b.append(i)
    return b


def get_missing_numbers2(l, min, max):
    return [i for i in range(min, max+1) if i not in l]


print(get_missing_numbers2(a, 1, 10))