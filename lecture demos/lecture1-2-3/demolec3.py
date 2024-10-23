import random
import threading
import string
import time

# Here we perform threadinf for the same prgram whichgenerates 1e7 random letters and 1e7 numbers
# then we calculate the time and compare between serial and threading .

def join_random_letters():

    letters = [random.choice(string.ascii_letters) for _ in range(int(1e7))]

    joined_letters = ''.join(letters)
    return joined_letters

def join_random_numbers():

    numbers = [random.randint(1,100) for _ in range(int(1e7))]
    total_sum = sum(numbers)
    return total_sum

total_start_time = time.time()

thread1 = threading.Thread(target = join_random_letters)
thread2 = threading.Thread(target = join_random_numbers)

total_end_time = time.time()
'''
 student@dsai3203-template:~/DSAI-3202-60106447$ /usr/bin/python3 /home/student/DSAI-3202-60106447/demolec2.py
Total time taken: 0.0011801719665527344 seconds
(base) student@dsai3203-template:~/DSAI-3202-60106447$ /usr/bin/python3 "/home/student/DSAI-3202-60106447/lecture demos/demolec2.py"
Total time taken: 1.9311904907226562e-05 seconds
(base) student@dsai3203-template:~/DSAI-3202-60106447$ /usr/bin/python3 "/home/student/DSAI-3202-60106447/lecture demos/demolec2.py"
Total time taken: 1.9073486328125e-05 seconds
(base) student@dsai3203-template:~/DSAI-3202-60106447$ 

'''
join_random_letters()
join_random_numbers()



print(f"Total time taken: {total_end_time - total_start_time} seconds")