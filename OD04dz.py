import time
import random

def quick_sort(s):
    if len(s) <= 1:
        return s

    element = s[0]
    left = list(filter(lambda i: i < element, s))
    center = [i for i in s if i == element]
    right = list(filter(lambda i: i > element, s))

    return quick_sort(left) + center + quick_sort(right)

def measure_sort_time(sort_func, array):
    start_time = time.perf_counter()
    sort_func(array)
    end_time = time.perf_counter()
    return end_time - start_time

def main():
    sizes = [10, 100, 1000, 5000, 10000, 20000]
    for size in sizes:
        array = [random.randint(0, 10000) for _ in range(size)]
        time_taken = measure_sort_time(quick_sort, array)
        print(f'Size: {size}, Time taken: {time_taken:.6f} seconds')

if __name__ == "__main__":
    main()