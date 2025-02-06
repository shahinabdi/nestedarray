import time
import sys
from memory_profiler import profile

@profile
def process_large_array(size):
    # Create a nested list structure
    nested_array = []
    for i in range(size):
        nested_array.append([j for j in range(100)])  # Each inner array has 100 elements
    
    # Process the array
    total = 0
    for i in range(len(nested_array)):
        for j in range(len(nested_array[i])):
            total += nested_array[i][j]
    
    return total

def main():
    sizes = [100, 1000, 10000]  # Different array sizes to test
    
    for size in sizes:
        print(f"\nTesting with array size: {size}")
        
        # Measure memory usage before
        start_mem = sys.getsizeof([])/1024/1024  # MB
        
        # Measure time
        start_time = time.time()
        result = process_large_array(size)
        end_time = time.time()
        
        # Memory after
        end_mem = sys.getsizeof([])/1024/1024  # MB
        
        print(f"Time taken: {end_time - start_time:.2f} seconds")
        print(f"Memory used: {end_mem - start_mem:.2f} MB")
        print(f"Result: {result}")

if __name__ == "__main__":
    main()