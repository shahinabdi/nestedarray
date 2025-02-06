import time
from memory_profiler import profile
from numba import jit
import psutil
import gc

# Pre-compute the inner list since it's always the same
INNER_LIST = list(range(100))

@profile
def process_large_array(size):
    # Use list comprehension for faster list creation
    # Reference the pre-computed inner list instead of recreating it
    nested_array = [INNER_LIST.copy() for _ in range(size)]
    
    # Use local variable access optimization
    total = 0
    # Use enumerate to avoid len() calls and separate index tracking
    for row in nested_array:
        # Use builtin sum for the inner loop - it's implemented in C and faster
        total += sum(row)
    
    return total

# JIT-compiled version for comparison while keeping nested structure
@jit(nopython=True)
def process_large_array_jit(size):
    # Create nested structure directly
    nested_array = [[j for j in range(100)] for _ in range(size)]
    
    total = 0
    for row in nested_array:
        for val in row:
            total += val
            
    return total

def get_memory_usage():
    """Get current memory usage in MB"""
    process = psutil.Process()
    return process.memory_info().rss / 1024 / 1024

def benchmark_versions(sizes):
    versions = [
        ("Optimized", process_large_array),
        ("JIT", process_large_array_jit)
    ]
    
    for size in sizes:
        print(f"\n=== Testing with array size: {size} ===")
        
        for name, func in versions:
            # Clear memory before each test
            gc.collect()
            
            # Measure initial memory
            start_mem = get_memory_usage()
            
            # Warmup for JIT
            if name == "JIT":
                _ = func(10)
            
            # Timing
            start_time = time.perf_counter()
            result = func(size)
            end_time = time.perf_counter()
            
            # Memory after
            end_mem = get_memory_usage()
            
            print(f"\n{name} version:")
            print(f"Time taken: {end_time - start_time:.6f} seconds")
            print(f"Memory used: {end_mem - start_mem:.2f} MB")
            print(f"Result: {result}")

def main():
    sizes = [10000, 100000, 1000000]
    print("Starting benchmark...")
    benchmark_versions(sizes)

if __name__ == "__main__":
    main()