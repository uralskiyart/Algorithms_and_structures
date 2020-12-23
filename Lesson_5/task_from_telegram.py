import timeit

def pie_parts(aa, bb):
    average = aa if aa >= bb else bb

    if average == aa and aa % bb == 0:
        return aa
    if average == bb and bb % aa == 0:
        return bb

    if average == aa:
        for i in range(aa * 2, (aa * bb) + 1, average):
            if i % bb == 0:
                return i
    else:
        for i in range(bb * 2, (aa * bb) + 1, average):
            if i % aa == 0:
                return i



print(pie_parts(82546920, 48539250))


print(timeit.timeit('pie_parts(825, 344)', number=100, globals=globals()))
print(timeit.timeit('pie_parts(8254692, 4853925)', number=100, globals=globals()))
# 8254692, 4853925