import timeit

def sum(max_num):
    sol = 0
    for i in range(1,max_num+1):
        sol += 1
    return sol

def sum_2(max_num):
    sol = 0
    i = 1
    while i < max_num:
        sol += 1
        i += 1
    return sol


def sum_3(max_num):
    return max_num * (max_num + 1)/2



print("Testing get sum - 1")

print(timeit.repeat(stmt="sum(1000000)", repeat=5, number=1, globals=globals()))

print(" Testing sum2 ")

print(timeit.repeat(stmt="sum_2(1000000)", repeat=5, number=1, globals=globals()))

print(" Testing sum3 ")

print(timeit.repeat(stmt="sum_3(1000000)", repeat=5, number=1, globals=globals()))

print( [x*2 for x in range(1,10)])

