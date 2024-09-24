import time

def calculate_sum(num):
    sum = 0
    for i in range(num+1):
        sum += i 
    return sum


n = 50000
start_time = time.time()
serial_sum = calculate_sum(n)
end_time = time.time()
print("The sum of all numbers from 1 to "+ str(n) +" = "+str(serial_sum))

print("The total time taken for excecution is: "+ str(end_time - start_time))