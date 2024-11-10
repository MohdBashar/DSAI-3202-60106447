# from tasks import power

# def dispatch_tasks():
#     result_objs = [power.apply_async((number, 2))
#                  for number in range(1, 10001)]
#     results = [result.get()
#          for result in result_objs]
#     return results
    
# if __name__ == "__main__":
#  results = dispatch_tasks()
#  print(results[:10])

# dispatch.py
import time
from tasks import power

def dispatch_tasks():
    # Start timing
    start_time = time.time()

    # Submit tasks asynchronously
    result_objs = [power.apply_async((number, 2)) for number in range(1, 10001)]

    # Retrieve task results
    results = [result.get() for result in result_objs]

    # End timing
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")

    return results

if __name__ == "__main__":
    results = dispatch_tasks()
    print(results[:10])  # Print the first 10 results
