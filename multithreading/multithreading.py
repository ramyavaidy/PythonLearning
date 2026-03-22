import time
import threading

def calculate_square(numbers):
    print("Calculating squares...")
    for n in numbers:
        time.sleep(0.5)  # Simulate a time-consuming task
        print(f"Square of {n} is {n * n}")

def calculate_cube(numbers):
    print("Calculating cubes...")
    for n in numbers:
        time.sleep(0.5)  # Simulate a time-consuming task
        print(f"Cube of {n} is {n * n * n}")

arr=[2,3,8,9]

t= time.time()
calculate_square(arr)
calculate_cube(arr)

print(f"Time taken without threading: {time.time() - t} seconds")

t= time.time()
t1= threading.Thread(target=calculate_square, args=(arr,))
t2= threading.Thread(target=calculate_cube, args=(arr,)) 

t1.start()
t2.start()

t1.join()
t2.join()   

print(f"Time taken with threading: {time.time() - t} seconds")