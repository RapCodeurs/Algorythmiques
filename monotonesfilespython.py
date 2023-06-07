a = [1, 5, 6, 9, 11, 11, 12, 15]
b = [1, 5, 6, 6, 5, 7, 10]

def is_increasing_monotonic_values(l):
    for i in range(len(l)-1):
        if l[i+1] < l[i]:
            return False
    return True


def is_increasing_monotonic_values2(l):
    return l == sorted(l)



print("a", is_increasing_monotonic_values2(a))
print("b", is_increasing_monotonic_values2(b))

