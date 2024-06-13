import random
import time
import timeit

list1 = []
start_time = 0
end_time = 0

def generate_rand_list(max_size):
    new_list = []
    for i in range(0,max_size):
        new_list.append(random.randint(1,99))
    return new_list


def bubble_sort(list):
    for i in range(len(list), 0, -1):
        for j in range(0,i-1):
           if list[j] > list[j+1]:
               swap = list[j]
               list[j] = list[j+1]
               list[j + 1] = swap


print("Testing Bubble Sort")
list1 = generate_rand_list(100)
start_time = time.time()
bubble_sort(list1)
print(f"time taken is {time.time() - start_time} seconds")


print("Testing Bubble Sort")
list1 = generate_rand_list(500)
start_time = time.time()
bubble_sort(list1)
print(f"time taken is {time.time() - start_time} seconds")



print("Testing Bubble Sort")
list1 = generate_rand_list(10000)
start_time = time.time()
bubble_sort(list1)
print(f"time taken is {time.time() - start_time} seconds")

bubble_sort(generate_rand_list(10))

