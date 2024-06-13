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

list1 = generate_rand_list(10)

print(list1)

def add_item_to_list(num):
    list1.append(num)

add_item_to_list(12)

print(list1)

def linear_search(val):
    val_found = "Value not found"
    for i in list1:
        if i == val:
            val_found = "Value Found"
    print(val_found)

print("Testing linear search")
list1 = generate_rand_list(2000)
start_time = time.time()
linear_search(100)
print(f"time taken is {time.time() - start_time} seconds")

print("Testing linear search")
list1 = generate_rand_list(200000)
start_time = time.time()
linear_search(100)
print(f"time taken is {time.time() - start_time} seconds")


print("Testing linear search")
list1 = generate_rand_list(2000000)
start_time = time.time()
linear_search(100)
print(f"time taken is {time.time() - start_time} seconds")

