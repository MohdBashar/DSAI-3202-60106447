import multiprocessing
import time
import random
import string # to use the string.ascii_letters method to generate the letters.

def join_random_numbers():
    ran = random.randint(1,100)
    for i in range(int(1e7)):
        numbers = []
        numbers.append(ran)
    total_sum = sum(numbers)
    print('Add numbers Task Done')

def join_random_letters():
    letters = [random.choice(string.ascii_letters) for _ in range(int(1e7))]
    joined_letters = "".join(letters)
    print("Joined letters Task Done")

total_serialstart_time = time.time()

join_random_letters()
join_random_numbers()

total_serialend_time = time.time()

print(f"Total time taken : {total_serialend_time - total_serialstart_time} seconds")


total_start_time = time.time()

process1 = multiprocessing.Process(target = join_random_letters)
process2 = multiprocessing.Process(target = join_random_numbers)

process1.start()
process2.start()

process1.join()
process2.join()

total_end_time = time.time()

print(f"Total time taken : {total_end_time - total_start_time} seconds")

