def triple_symmetric_difference(a, b, c):
    all_elements = a | b | c
    return {x for x in all_elements if (x in a) + (x in b) + (x in c) == 1}

a = {1,2,3,4}
b = {2,4,5,6}
c = {3,4,6,7}

print((a^b^c)-(a&b&c))
